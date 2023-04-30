books ={}
#Write a Python function that takes the following parameters:books (a dictionary) - A dictionary of books with the ISBN as the key and the value as another dictionary containing the book's title, author, and publication date.

# isbn (a string) - The ISBN of the book to be added to the books dictionary.
# title (a string) - The title of the book to be added.
#author (a string) - The author of the book to be added.
#publication_date (a string) - The publication date of the book to be added.

#The function should add the new book to the books dictionary using the given ISBN as the key and a dictionary containing the title, author, and publication date as the value.

def main():
    while True:
        choice = menu()
        if choice == 1:
            noOfBooks = int(input('Number of Books: '))
            for i in range(noOfBooks):
                isbn = input('ISBN: ')
                title = input('Title: ')
                author = input('Author: ')
                publication_date = input('Publication Date: ')
                print(addBook(books,isbn,title,author,publication_date))
        elif choice == 2:
            removeBook(books,input('Enter ISBN:'))
        elif choice == 3:
            deleteDictionary(books)
        elif choice == 4:
           print(searchBook(books,input('Author name: ')))
        elif choice == 5:
            insertItem(books)
        elif choice == 6:
            updateItems(books)
        elif choice == 7:
            count = countItems(books)
            print(f'Number of books : {count}')
        print('Y/y OR N/n' ,end='')
        c = input()
        if c == 'Y' or c == 'y':
            continue
        else:
            break   
def menu():
    print('1. Create Dictionary of Books')
    print('2. Remove a book from Dictionary.')
    print('3. Delete Dictionary')
    print('4. Search specific item from dictionary.')
    print('5. Insert a book to dictionary.')
    print('6. Update a specific value from dictionary. (e.g update title of book).')
    print('7. Count number of items in dictionary.')
    choice = int(input())
    return choice
def addBook (books,isbn, title, author, publication_date ):
    if isbn not in books:
        books[isbn] = {
            'title' : title,
            'author' : author,
            'publication_date' : publication_date
        }  
    else:
        print('Book repetition not allowed!')
    return books
def removeBook(books,isbn):
    if isbn in books:
        del books[isbn]
        print('Book Removed Successfully!')
    else:
        print("The book doesn't exist")
    print(books)
def deleteDictionary(books):
    del books
    print('Dictionary Deleted!')
def searchBook(books,author):
    return [book for book in books.values() if book['author'] == author]
def insertItem(books):
    while True: 
        isbn = input('ISBN: ')
        if isbn not in books:
            title = input('Title: ')
            author = input('Author: ')
            publication_date = input('Publication Date: ')
            addBook(books,isbn, title, author, publication_date )
            break
        else:
            print('Book already exists!')
            continue
def updateItem(books):
    isbn_ToUpdate = input ('ISBN: ')
    if isbn_ToUpdate in books:
        updateKey = input('What you want to update? ').lower()
        updateValue = input(f'New Value of {updateKey}: ')
        books [isbn_ToUpdate] [updateKey] = updateValue
        print('Book Updated !!')
    else: 
        print('Book NOT found!')
    print (books)
def countItems(books):
    return len(books)
main()