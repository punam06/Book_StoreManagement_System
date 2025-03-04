def remove_books(all_books):
    isbn = input("Enter the ISBN of the book to remove: ")
    for book in all_books:
        if book['ISBN'] == isbn:
            all_books.remove(book)
            print("Book removed successfully!")
            return all_books
    print("Book not found.")
    return all_books