import sqlite3

# Open (create) new database
db = sqlite3.connect("books-collection.db") 

# Create cursor to control database
cursor = db.cursor()

# Create table. (Database can contain many tables)
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
    # cursor - created in previous step
    # .execute() - execute commands https://www.codecademy.com/article/sql-commands
    # CREATE TABLE books - název "books"
    # () - column headings; varchar - variable length string max. 250, NOT NULL - cannot be empty, UNIQUE

# Add data to table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()