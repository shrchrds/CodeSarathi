import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
#create table 
c.execute('''CREATE TABLE IF NOT EXISTS Customers(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL,
phone INTEGER NOT NULL)''')
conn.commit()
#insert data
c.execute("INSERT INTO Customers (name, email, phone) VALUES ('Vijay', 'vijay@gmail.com', 8527396010)")
c.execute("INSERT INTO Customers (name, email, phone) VALUES ('Suhas', 'suhas@gmail.com', 9843215678)")
#select data
for row in c.execute('SELECT * FROM Customers'):
    print(row)
#update
c.execute("UPDATE Customers SET name = 'Sagar' WHERE id = 2")
conn.commit()
print("After Name Change: ")
for row in c.execute('SELECT * FROM Customers WHERE id = 2'):
    print(row)
#delete
c.execute("DELETE FROM Customers WHERE id = 3")
print("After Deleting ID: ")
for row in c.execute('SELECT * FROM Customers'):
    print(row)
conn.commit()
conn.close()