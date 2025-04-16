import sqlite3
from pathlib import Path
cwd = Path.cwd()
print(cwd)
connection = sqlite3.connect("booksDataBase.db")
connection.row_factory = sqlite3.Row

def displayAllBooks():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    for row in cursor:
            if row["isBorrowed"] == True:
                print(f'   {row["title"]} - {row["author"]} is borrowed')
            elif row["isBorrowed"] == False:
                 print(f'   {row["title"]} - {row["author"]} is available')
    cursor.close()

def diaplayAvailableBooks():
    cursor = connection.cursor()
    cursor.execute("SELECT title,isBorrowed,author FROM books WHERE isBorrowed = False")
    for row in cursor:
           print(f'   "{row["title"]}" by {row["author"]} is available')
    cursor.close()

def updateBookBorrowed(chosenId):
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET isBorrowed=True  WHERE id = ?",(chosenId,))
    connection.commit()
    cursor.close()

def updateBookReturned(chosenId):
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET isBorrowed=False  WHERE id = ?",(chosenId,))
    connection.commit()
    cursor.close()

def returnBooksByAuthor(chosenAut):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE author = ?",(chosenAut,))
    booksWritenAuthor = []
    for row in cursor:
        print(f'"{row["title"]}" by {row["author"]}')  
    cursor.close()

def deleteBook(chosenTitle):
     cursor = connection.cursor()
     cursor.execute("DELETE FROM books WHERE title = ?",(chosenTitle,))
     connection.commit()
     cursor.close()

def countBorrowedBooks():
    cursor = connection.cursor()
    cursor.execute("SELECT title FROM books WHERE isBorrowed = True")
    borrowedBooks = []
    for i in cursor:
         borrowedBooks.append(i)
    return len(borrowedBooks)

def orderByTitle():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books ORDER BY title")
    for row in cursor:
            if row["isBorrowed"] == True:
                print(f'   {row["title"]} - {row["author"]} is borrowed')
            elif row["isBorrowed"] == False:
                 print(f'   {row["title"]} - {row["author"]} is available')
    cursor.close()




cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("CREATE TABLE books (id INT, title STRING, author STRING, isBorrowed BOOLEAN)")
cursor.execute("""
                  INSERT INTO books VALUES 
                  ('1','Quest Of The Sunfish - Escape To The Moon Islands', 'Mardi McConnochie', True),
                  ('2','How To Survive On Mars', 'Jasmina Lazendic-Galloway', False),
                  ('3','One Piece - Volume 1','Eiichiro Oda',False),
                  ('4','Harry Potter and the Philosopher''s Stone','J.K. Rowling',False),
                  ('5','The Lord of the Rings','John Ronald Reuel Tolkien',False),
                  ('6','The Cuckroo''s Calling','J.K. Rowling', True)
               """)
connection.commit()
cursor.close()



print("\nAll the books:")
displayAllBooks()
print("\n\n\n")

print("Available books:")
diaplayAvailableBooks()
print("\n\n\n")

updateBookBorrowed(3)
updateBookReturned(6)
print("One piece is borrowed, and The Cuckroo's Calling is returned.\nNew list:")
displayAllBooks()
print("\n\n\n")


print("Books written by J.K. Rowling are:")
print(returnBooksByAuthor("J.K. Rowling"))
print("\n\n\n")


deleteBook('The Lord of the Rings')
print("Lord of the Rings is deleted.\nNew list:")
displayAllBooks()
print("\n\n\n")

print(f'{countBorrowedBooks()} book(s) is borrowed right now.\n\n\n')

print("These are the books, ordered alphabetically")
orderByTitle()