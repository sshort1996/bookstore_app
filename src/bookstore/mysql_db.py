import mysql.connector
import functools
from dataclasses import dataclass
import os
from faker import Faker
import random


class myDB:

    def __init__(self, reset=False):
        # Replace the placeholders with your actual values
        host = "localhost"
        user = "root"
        password = os.environ["MY_SQL_PW"]
        database = "mysql"

        # Establish connection to the MySQL server
        self.cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object to execute SQL queries
        self.csr = self.cnx.cursor()

        # run database setup code 
        self.__call__("SHOW DATABASES;")
        self.__call__("SELECT DATABASE();")
        self.__call__("CREATE DATABASE IF NOT EXISTS bookstore;")
        self.__call__("USE bookstore;")
        if reset == True: 
            self.__call__("DROP TABLE books;")  

    def __call__(self, query, values=None, print_output = False, cursor = None):
        
        if cursor is None:
            cursor = self.csr

        results = ()
        try:
            
            # cursor.execute(query)
            
            if values:
                formatted_query = query % tuple(values)
                print(f"executing: {formatted_query}")
                cursor.execute(query, values)
            else: 
                print(f'executing: {query}')
                cursor.execute(query)

            # Retrieve the results (if any)
            results = cursor.fetchall()
            
            if print_output:
                for row in results:
                    print(row)

        except Exception as err: 
            print(f"An error occurred: {err}")
        
        return results


def map_types(cls):
  
    for field_name, field_type in cls.__annotations__.items():
        mysql_type = cls.type_mapping.get(field_type)
        if mysql_type is None:
            raise ValueError(f"Unsupported data type: {field_type} for field {field_name}")
        setattr(cls, field_name, field_type)  # Set the original field type
        setattr(cls, f"__mysql_{field_name}_type__", mysql_type)  # Add the MySQL data type attribute
    return cls

# Usage:
@map_types
@dataclass
class Book:
    id: int
    title: str
    price: float
    type_mapping = {
        int: 'INT',
        str: 'VARCHAR(255)',
        float: 'DECIMAL(10,2)'
    }

    def insert(self, db_inst):

        columns = []
        values = []
        
        for field in self.__dataclass_fields__.values():
            column_name = field.name
            attr_value = getattr(self, column_name)
            columns.append(column_name)
            if isinstance(attr_value, str):  # Check if attribute value is a string
                attr_value = f"'{attr_value}'"
            values.append(str(attr_value))
        
        query = f"INSERT INTO books ({', '.join(columns)}) VALUES ({', '.join(values)})"
        db_inst(query)
        db_inst.cnx.commit()

    @classmethod
    def create_table(cls, db_inst):
        fields = []
        for field_name, field_type in cls.__annotations__.items():
            mysql_type = getattr(cls, f"__mysql_{field_name}_type__")
            fields.append(f"{field_name} {mysql_type}")

        create_tbl = f"CREATE TABLE IF NOT EXISTS books ({', '.join(fields)});"
        db_inst(create_tbl)


def generate_book_titles(num_titles):
    fake = Faker()
    return [fake.catch_phrase() for _ in range(num_titles)]
    


def generate_book_price(num_titles):
    return [(float(random.randint(12, 50))*0.5) - 0.01 for _ in range(num_titles)]


if __name__ == "__main__":

    mydb = myDB(reset=True)
    Book.create_table(mydb)

    # Generate 10 random book titles
    book_titles = generate_book_titles(250)
    book_prices = generate_book_price(250)
    
    for index, (title, price) in enumerate(zip(book_titles, book_prices)):
        print(f"Book  {title} - ${price}")
        book = Book(index+1, title, price)
        book.insert(mydb)

    mydb('select * from books')

    # Close the cursor and the connection
    mydb.csr.close()
    mydb.cnx.close()
