def view_all_books(all_books):
    if not all_books:
        print("No books available.")
        return

    for index, book in enumerate(all_books, start=1):
        print(f"{index}. Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Genre: {book['Genre']}, Price: {book['Price']}, Quantity: {book['Quantity']}")