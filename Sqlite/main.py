import sqlite3

conn = sqlite3.connect("data.db")
print("Connected database")

c = conn.cursor()

# c.execute('''CREATE TABLE book (name STR, number INT, price FLOAT)''')
# print("Table created successfully")

#    book_name = str(input("Enter book name: "))
#   book_number = int(input("Enter book number: "))
#  price = float(input("Enter price: "))

# c.execute('''INSERT INTO book VALUES (?,?,?)''', (book_name, book_number, price))
# conn.commit()
# print("Data created Successfully")

c.execute('''SELECT number FROM book''')
results = c.fetchall()

print("\n")
for row in results:
    print(row)
