import csv

def save_books(all_books):
    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'ISBN', 'Genre', 'Price', 'Quantity'])
        for book in all_books:
            writer.writerow([book['Title'], book['Author'], book['ISBN'], book['Genre'], book['Price'], book['Quantity']])
    print("Books saved successfully!")

def load_books():
    try:
        with open('books.csv', 'r') as file:
            reader = csv.DictReader(file)
            books = []
            for row in reader:
                row['Price'] = float(row['Price'])
                row['Quantity'] = int(row['Quantity'])
                books.append(row)
            return books
    except FileNotFoundError:
        print("No saved books found. Starting fresh.")
        return []