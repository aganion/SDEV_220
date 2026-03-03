"""
Alicia Ganion
M4 Programming Assignment 2
March 1, 2026
"""

#23.1
lines_books = [
    "author,book",
    "J R R Tolkien,The Hobbit",
    'Lynne Truss,"Eats, Shoots & Leaves"'
]

with open("books.csv", "w", newline="") as f:
    for line in lines_books:
        f.write(line + "\n")

#23.2
import csv
with open("books.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    books = list(reader)

print("Books read from books.csv: ")
print(books)

#23.3
lines_books2 = [
    "title,author,year",
    "The Weirdstone of Brisingamen,Alan Garner,1960",
    "Perdido Street Station,China Miéville,2000",
    "Thud!,Terry Pratchett,2005",
    "The Spellman Files,Lisa Lutz,2007",
    "Small Gods,Terry Pratchett,1992"
]

with open("books2.csv", "w", newline="") as f:
    for line in lines_books2:
        f.write(line + "\n")

#23.4
import sqlite3

conn = sqlite3.connect("books.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

conn.commit()

#23.5
cur.execute("DELETE FROM books")
conn.commit()

with open("books2.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute(
            "Insert INTO books (title, author, year) VALUES (?, ?, ?)",
            (row["title"], row["author"], row["year"])
        )

conn.commit()

#23.6
cur.execute("SELECT title FROM books ORDER BY title")
titles_alphabet = [row[0] for row in cur.fetchall()]
print("\nTitles in alphabetical order:")
print(titles_alphabet)

#23.7
cur.execute("SELECT title, author, year FROM books ORDER BY year")
books_by_year = cur.fetchall()
print("\nBooks ordered by publication year:")
for book in books_by_year:
    print(book)

cur.close()
conn.close()

#23.8

import sqlalchemy as sa

conn = sa.create_engine('sqlite:///books.db')
with conn.connect() as conn:
    query = sa.text("SELECT title FROM books ORDER BY title")
    result = conn.execute(query)
    titles = [row[0] for row in result.fetchall()]
print("Titles in alphabetical order (SQLAlchemy):")
print(titles)