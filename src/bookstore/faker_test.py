from faker import Faker

def generate_book_titles(num_titles):
    fake = Faker()
    book_titles = [fake.catch_phrase() for _ in range(num_titles)]
    return book_titles

# Generate 10 random book titles
book_titles = generate_book_titles(10)

# Print the generated book titles
for title in book_titles:
    print(title)
