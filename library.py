import add_books
import view_all_books
import update_books
import remove_books
import save_all_books
import search_books

# Load existing books from file
all_books = save_all_books.load_books()

while True:
    print(f"\nWelcome to our Library Management System! Please select a menu ID: ")
    print("Menu ID = 1. Add a New Book.")
    print("Menu ID = 2. Update your Book.")
    print("Menu ID = 3. Remove a Selected Book.")
    print("Menu ID = 4. View All Books.")
    print("Menu ID = 5. Search Books.")
    print("Menu ID = 6. Exit")
    
    menu = input(f"\nSelect any Number: ")
    if menu == "1":
        all_books = add_books.add_books(all_books)  # Ensure the add_books function returns the updated list
    elif menu == "2":
        all_books = update_books.update_books(all_books)  # Ensure the update_books function returns the updated list
    elif menu == "3":
        all_books = remove_books.remove_books(all_books)  # Ensure the remove_books function returns the updated list
    elif menu == "4":
        view_all_books.view_all_books(all_books)  # This function might not need to return anything
    elif menu == "5":
        print("Search by: 1. Title 2. Author 3. Price 4. Genre")
        search_option = input("Select search option: ")
        if search_option == "1":
            title = input("Enter the book title: ")
            results = search_books.search_by_title(all_books, title)
            search_books.display_search_results(results)
        elif search_option == "2":
            author = input("Enter the book author: ")
            results = search_books.search_by_author(all_books, author)
            search_books.display_search_results(results)
        elif search_option == "3":
            min_price = float(input("Enter the minimum price: "))
            max_price = float(input("Enter the maximum price: "))
            results = search_books.search_by_price(all_books, min_price, max_price)
            search_books.display_search_results(results)
        elif search_option == "4":
            genre = input("Enter the book genre: ")
            results = search_books.search_by_genre(all_books, genre)
            search_books.display_search_results(results)
        else:
            print("Invalid search option.")
    elif menu == "6":
        save_all_books.save_books(all_books)
        print(f"\nThanks for using our Library Management System!")
        break
    else:
        print("Please select a valid number.")