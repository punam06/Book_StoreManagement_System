def search_by_title(all_books, title):
    results = [book for book in all_books if title.lower() in book['Title'].lower()]
    return results

def search_by_author(all_books, author):
    results = [book for book in all_books if author.lower() in book['Author'].lower()]
    return results

def search_by_price(all_books, min_price, max_price):
    results = [book for book in all_books if min_price <= float(book['Price']) <= max_price]
    return results

def search_by_genre(all_books, genre):
    results = [book for book in all_books if genre.lower() in book['Genre'].lower()]
    return results

def display_search_results(results):
    if not results:
        print("No books found.")
    else:
        for book in results:
            print(f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Genre: {book['Genre']}, Price: {book['Price']}, Quantity: {book['Quantity']}")