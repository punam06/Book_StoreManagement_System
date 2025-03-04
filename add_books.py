def add_books(all_books):
    title = input("Enter the book title: ")
    if not title:
        print("The book title must be a non-empty string.")
        return all_books

    author = input("Enter the book author: ")
    if not author:
        print("The book author must be a non-empty string.")
        return all_books

    isbn = input("Enter the book ISBN: ")
    if not isbn:
        print("The book ISBN must be a non-empty string.")
        return all_books

    genre = input("Enter the book genre: ")
    if not genre:
        print("The book genre must be a non-empty string.")
        return all_books

    try:
        price = float(input("Enter the book price: "))
        if price <= 0:
            print("The price must be a positive number.")
            return all_books
    except ValueError:
        print("The price must be a valid number.")
        return all_books

    try:
        quantity = int(input("Enter the quantity in stock: "))
        if quantity < 0:
            print("The quantity must be a non-negative integer.")
            return all_books
    except ValueError:
        print("The quantity must be a valid integer.")
        return all_books

    # Check for duplicate ISBN
    for book in all_books:
        if book['ISBN'] == isbn:
            print("A book with this ISBN already exists.")
            return all_books

    new_book = {
        'Title': title,
        'Author': author,
        'ISBN': isbn,
        'Genre': genre,
        'Price': price,
        'Quantity': quantity
    }

    all_books.append(new_book)
    print("Book added successfully!")
    return all_books