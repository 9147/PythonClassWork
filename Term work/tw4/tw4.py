'''
Write a Python program to perform the following:
a. Create a database named “products.db”
b. Create a table named “products” that has the following fields:
prodID: int
name: text
quantity: int
price: real
c. Insert n records into the table reading the values for each item from the user.
d. Display the recordset after fetching all the rows.
e. Delete a product whose product ID is entered by the user.
f. Increase the price of all products whose current price is less than Rs.50, by 10%.
g. Display all the products whose quantity is less than 40.
'''


import sqlite3

# Create a database and connect to it
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Create the 'products' table
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    prodID INTEGER PRIMARY KEY,
                    name TEXT,
                    quantity INTEGER,
                    price REAL
                )''')


# Function to insert records into the table
def insert_record():
    n = int(input("Enter the number of records to insert: "))
    for _ in range(n):
        prodID = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        cursor.execute("INSERT INTO products (prodID, name, quantity, price) VALUES (?, ?, ?, ?)",
                       (prodID, name, quantity, price))
        conn.commit()


# Function to display all records
def display_records():
    cursor.execute("SELECT * FROM products")
    records = cursor.fetchall()
    for record in records:
        print(record)


# Function to delete a product by product ID
def delete_product():
    prodID = int(input("Enter the product ID to delete: "))
    cursor.execute("DELETE FROM products WHERE prodID = ?", (prodID,))
    conn.commit()
    print("Product deleted successfully.")


# Function to increase the price of products under Rs.50 by 10%
def increase_price():
    cursor.execute("UPDATE products SET price = price * 1.1 WHERE price < 50")
    conn.commit()
    print("Prices increased for eligible products.")


# Function to display products with quantity less than 40
def display_low_quantity_products():
    cursor.execute("SELECT * FROM products WHERE quantity < 40")
    records = cursor.fetchall()
    for record in records:
        print(record)


# Main program
while True:
    print("\nMenu:")
    print("1. Insert records")
    print("2. Display records")
    print("3. Delete a product")
    print("4. Increase price of products under Rs.50")
    print("5. Display products with quantity less than 40")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_record()
    elif choice == 2:
        display_records()
    elif choice == 3:
        delete_product()
    elif choice == 4:
        increase_price()
    elif choice == 5:
        display_low_quantity_products()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please select a valid option.")

# Close the connection
conn.close()
