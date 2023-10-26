import mysql.connector
import functools
from dataclasses import dataclass, field
import os
from faker import Faker
import random
from typing import Type
import bcrypt


class myDB:
    """
    A class representing a database connection and query execution.

    Attributes:
        cnx: The connection to the MySQL server.
        csr: The cursor object to execute SQL queries.
    """

    def __init__(self, reset: bool = False) -> None:
        """
        Initializes a new instance of the myDB class.

        Args:
            reset: Flag indicating whether to reset the database (default: False).
        """
        # Replace the placeholders with your actual values
        host: str = "localhost"
        user: str = "root"
        password: str = os.environ["MY_SQL_PW"]
        database: str = "mysql"

        # Establish connection to the MySQL server
        self.cnx: mysql.connector.connection.MySQLConnection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object to execute SQL queries
        self.csr: mysql.connector.cursor.MySQLCursor = self.cnx.cursor()

        # Run database setup code 
        self.__call__("SHOW DATABASES;")
        self.__call__("SELECT DATABASE();")
        self.__call__("CREATE DATABASE IF NOT EXISTS bookstore;")
        self.__call__("USE bookstore;")
        if reset:
            self.__call__("DROP TABLE books;")
            self.__call__("DROP TABLE users;")


    def __call__(self, query: str, values: tuple = None, print_output: bool = False, print_results: bool = False, cursor: mysql.connector.cursor.MySQLCursor = None) -> tuple:
        """
        Executes an SQL query and returns the results (if any).

        Args:
            query: The SQL query to execute.
            values: The values to be inserted into the query (optional).
            print_output: Flag to print the formatted query before execution (default: False).
            print_results: Flag to print the query results after execution (default: False).
            cursor: The cursor object to use for query execution (default: self.csr).

        Returns:
            The results of the query as a tuple.
        """
        if cursor is None:
            cursor = self.csr

        results = ()
        try:
            if values:
                formatted_query = query % tuple(values)
                if print_output:
                    print(f"executing: {formatted_query}")
                    print('-' * 60)
                cursor.execute(query, values)
            else:
                if print_output:
                    print(f"executing: {query}")
                    print('-' * 60)
                cursor.execute(query)

            # Retrieve the results (if any)
            results = cursor.fetchall()

            if print_results:
                for row in results:
                    print(row)

        except Exception as err:
            print(f"An error occurred: {err}")

        return results


def map_types(cls: Type) -> Type:
    """
    Maps the annotated field types to MySQL data types.

    Args:
        cls: The class to map the field types for.

    Returns:
        The modified class with mapped field types.
    """
    for field_name, field_type in cls.__annotations__.items():
        mysql_type = cls.type_mapping.get(field_type)
        if mysql_type is None:
            raise ValueError(f"Unsupported data type: {field_type} for field {field_name}")
        setattr(cls, field_name, field_type)  # Set the original field type
        setattr(cls, f"__mysql_{field_name}_type__", mysql_type)  # Add the MySQL data type attribute
    return cls


@map_types
@dataclass
class Table:
    """
    A base class representing a table in the database.

    Attributes:
        type_mapping: A dictionary mapping Python data types to MySQL data types.
    """

    type_mapping = {
        int: 'INT',
        str: 'VARCHAR(255)',
        float: 'DECIMAL(10,2)',
        bool: 'BOOL'
    }


    def insert(self, db_inst) -> None:
        """
        Inserts a new record into the table.

        Args:
            db_inst: The instance of myDB class to execute the query.

        Returns:
            None.
        """
        columns = []
        values = []
        upsert = False
        # print(f'self.__dataclass_fields__.values(): {self.__dataclass_fields__.values()}')
        for field in self.__dataclass_fields__.values():
            column_name = field.name
            attr_value = getattr(self, column_name)
            # print(field.metadata.get('primary_key', False))
            if column_name == 'id' and self.id:
                print(f'id passed to insert method - column_name: {column_name} attr_value: {attr_value}')
                upsert = True
                columns.append(column_name)
                values.append(str(attr_value))

            if not field.metadata.get('primary_key', False):
                columns.append(column_name)

            if column_name == 'salt':
                salt = bcrypt.gensalt()
                attr_value = salt.decode('utf-8')
                print(f'salt: {salt}')

            if field.metadata.get('hashed', False): 

                # Hash a string with the generated salt
                password = attr_value.encode('utf-8')  # Convert the password string to bytes
                print(f'salt: {salt}')
                print(f'password: {password}')
                attr_value = bcrypt.hashpw(password, salt).decode('utf-8')

            if isinstance(attr_value, str):  # Check if attribute value is a string
                attr_value = f"'{attr_value}'"

            if not field.metadata.get('primary_key', False):
                values.append(str(attr_value))

        table_name = self.__class__.__name__.lower()
        if upsert:
            merge_string = [f'{column}=VALUES({column})' for column in columns]
            query = f"""
                INSERT INTO {table_name} 
                ({', '.join(columns)}) 
                VALUES ({', '.join(values)})
                ON DUPLICATE KEY UPDATE 
                {', '.join(merge_string)};
                """
        else:
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)})"
        print(f'insert method: {query}')
        db_inst(query)
        db_inst.cnx.commit()


    @classmethod
    def create_table(cls, db_inst, print_output=False) -> None:
        """
        Creates the table in the database.

        Args:
            db_inst: The instance of myDB class to execute the query.
            print_output: Flag to print the query before execution (default: False).

        Returns:
            None.
        """
        fields = []
        for field_name, field_type in cls.__annotations__.items():
            mysql_type = cls.type_mapping.get(field_type)
            if mysql_type is not None and field_name != 'id':
                fields.append(f"{field_name} {mysql_type}")

        table_name = cls.__name__.lower()
        create_tbl = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT, {', '.join(fields)}, PRIMARY KEY (id));"
        db_inst(create_tbl, print_output=print_output)


    def read(self, db_inst, **kwargs):
        """
        Retrieves records from the table based on the given conditions.

        Args:
            db_inst: The instance of myDB class to execute the query.
            **kwargs: Optional keyword arguments representing conditions.

        Returns:
            A list of dictionary objects representing the retrieved records.
        """
        if 'where' in kwargs.keys(): 
            where_clause = f" WHERE {kwargs['where']}"
        elif kwargs:
            conditions = [f"{column} = '{value}'" for column, value in kwargs.items()]
            where_clause = " WHERE " + " AND ".join(conditions)
        else:
            where_clause = ""

        table_name = self.__class__.__name__.lower()
        query = f"SELECT * FROM {table_name}{where_clause}"
        print(query)
        try:
            results = db_inst(query, values = kwargs['values'])
        except KeyError as err:
            results = db_inst(query)
            print(err)

        columns = [field.name for field in self.__dataclass_fields__.values()]

        result_objects = []
        for row in results:
            row_dict = {}
            for column, value in zip(columns, row):
                field_type = self.__annotations__[column]
                if field_type == int:
                    value = int(value)
                elif field_type == bool:
                    value = bool(value)
                row_dict[column] = value
            dict_element = self.__class__(**row_dict)

            result_objects.append(dict_element)

        if len(result_objects) == 1:
            return dict_element

        return result_objects


@dataclass
class Books(Table):
    """
    A class representing the Books table.

    Attributes:
        id: The ID of the book.
        title: The title of the book.
        price: The price of the book.
        primary_key: The primary key field (default: 'id').
    """

    id: int = field(default=0, metadata={'primary_key': True})
    title: str = field(default='')
    price: float = field(default=0.0)
    # primary_key: str = field(default='id')


    @classmethod
    def create_table(cls, db_inst, print_output=False) -> None:
        """
        Creates the Books table in the database.

        Args:
            db_inst: The instance of myDB class to execute the query.
            print_output: Flag to print the query before execution (default: False).

        Returns:
            None.
        """
        super().create_table(db_inst, print_output)
        # Add additional logic specific to the Books table if needed


    def __repr__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            The string representation of the object.
        """
        attributes = ", ".join([f"  \n  - {attr}: {getattr(self, attr)}" for attr in self.__dict__])
        return f"\n \n {attributes}"


    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            The string representation of the object.
        """
        return self.__repr__()


@dataclass
class Users(Table):
    """
    A class representing the Users table.

    Attributes:
        id: The ID of the user.
        username: The username of the user.
        password: The password of the user.
        full_name: The full name of the user.
        email: The email address of the user.
        phone_number: The phone number of the user.
        home_address: The home address of the user.
        is_admin: Flag to indicate if the user is an admin.
        primary_key: The primary key field (default: 'id').
    """

    id: int = field(default=0, metadata={'primary_key': True})
    username: str = field(default='')
    salt: str = field(default='')
    password: str = field(default='', metadata={'hashed': True})
    full_name: str = field(default='', metadata={'PII': True})
    email: str = field(default='', metadata={'PII': True})
    phone_number: str = field(default='', metadata={'PII': True})
    home_address: str = field(default='', metadata={'PII': True})
    is_admin: bool = field(default=False)
    # primary_key: str = field(default='id')
    # hashed_fields: str = field(default)

    @classmethod
    def create_table(cls, db_inst, print_output=False):
        """
        Creates the Users table in the database.

        Args:
            db_inst: The instance of myDB class to execute the query.
            print_output: Flag to print the query before execution (default: False).

        Returns:
            None.
        """
        super().create_table(db_inst, print_output)
        # Add additional logic specific to the Users table if needed


    def __repr__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            The string representation of the object.
        """
        attributes = ", ".join([f"  \n  - {attr}: {getattr(self, attr)}" for attr in self.__dict__])
        return f"\n \n {attributes}"


    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            The string representation of the object.
        """
        return self.__repr__()


def generate_book_titles(num_titles):
    """
    Generates a list of random book titles.

    Args:
        num_titles: The number of titles to generate.

    Returns:
        A list of randomly generated book titles.
    """
    fake = Faker()
    return [fake.catch_phrase() for _ in range(num_titles)]
    

def generate_book_price(num_titles):
    """
    Generates a list of random book prices.

    Args:
        num_titles: The number of prices to generate.

    Returns:
        A list of randomly generated book prices.
    """
    return [(float(random.randint(12, 50))*0.5) - 0.01 for _ in range(num_titles)]


if __name__ == "__main__":

    mydb = myDB(reset=True)
    
    # Create Books table
    Books.create_table(mydb, print_output=True)
    
    # Generate 250 random book titles and prices
    book_titles = generate_book_titles(250)
    book_prices = generate_book_price(250)
    
    # Insert books into the database
    for index, (title, price) in enumerate(zip(book_titles, book_prices)):
        book = Books(title=title, price=price)
        book.insert(mydb)

    # Create Users table
    Users.create_table(mydb, print_output=True)
    
    # Insert user into the database
    user = Users(username='ShaneShort', 
                password='FastBoatsMojitos',     
                full_name='Shane Short',
                email='shane.short@gmail.com',
                phone_number='+61473519300',
                home_address='Unit 13, 1 High Street, Fremantle, WA 6160',
                is_admin=True)
    user.insert(mydb)

    # Insert another user into the database
    user = Users(username='test_user', 
                password='password',     
                full_name='John Doe',
                email='example@example.com',
                phone_number='123 456 7890',
                home_address='Unit 1, 1 Street Street, Townsville, Nairobi',
                is_admin=False)
    user.insert(mydb)

    # Read all users from the database
    print(user.read(mydb))
    
    # test update method 

    # Insert another user into the database
    user = Users(id = 2,
                username='test_user', 
                password='password',     
                full_name='John Doe',
                email='new_email@example.com',
                phone_number='123 456 7890',
                home_address='Unit 1, 1 Street Street, Townsville, Nairobi',
                is_admin=False)
    user.insert(mydb)
    print(user.read(mydb))

    # Read specific user from the database and check if they are an admin
    print(f"is test_user an admin?: {user.read(mydb, username='test_user').is_admin}")
    print(f"filter with fns:")
    print(user.read(mydb, where="upper(username)='TEST_USER'"))

    
    # test password verification
    hashed_passwords = [attr.password for attr in user.read(mydb)]
    passwords = ['FastBoatsMojitos', 'password']
    print(f'passwords: {hashed_passwords}')
    for password, hashed_password in zip(passwords, hashed_passwords):
        # Verify the hashed password
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            print("Password is correct!")
        else:
            print("Password is incorrect.")

    # Search for books with a price of '5.99'
    print(book.read(mydb, price='5.99'))

    # Close the cursor and the connection
    mydb.csr.close()
    mydb.cnx.close()
