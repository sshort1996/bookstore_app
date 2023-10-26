# from faker import Faker

# def generate_book_titles(num_titles):
#     fake = Faker()
#     book_titles = [fake.catch_phrase() for _ in range(num_titles)]
#     return book_titles

# # Generate 10 random book titles
# book_titles = generate_book_titles(10)

# # Print the generated book titles
# for title in book_titles:
#     print(title)

# import bcrypt

# # Generate a salt
# salt = bcrypt.gensalt()

# # Hash a string with the generated salt
# password = "my_password".encode('utf-8')  # Convert the password string to bytes
# hashed_password = bcrypt.hashpw(password, salt)

# # Verify the hashed password
# if bcrypt.checkpw(password, hashed_password):
#     print("Password is correct!")
# else:
#     print("Password is incorrect.")

table_name = 'test_table'
columns = ['col_a', 'col_b', 'col_c']
values = ['val_a', 'val_b', 'val_c']
merge_string = [f'{column}=VALUES({column})' for column in columns]
query = f"""
    INSERT INTO {table_name} 
    ({', '.join(columns)}) 
    VALUES ({', '.join(values)})
    ON DUPLICATE KEY UPDATE 
    {', '.join(merge_string)};
    """
print(query)