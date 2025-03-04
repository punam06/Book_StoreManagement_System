def update_books(all_books):
    isbn = input("Enter the ISBN of the book to update: ")
    for book in all_books:
        if book['ISBN'] == isbn:
            book['Title'] = input("Enter the new title: ")
            book['Author'] = input("Enter the new author: ")
            book['Genre'] = input("Enter the new genre: ")
            book['Price'] = float(input("Enter the new price: "))
            book['Quantity'] = int(input("Enter the new quantity: "))
            print("Book updated successfully!")
            return all_books
    print("Book not found.")
    return all_books