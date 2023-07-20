'''
    write a python program to read the book information from the user and store in a CSV file containing rows in the following format:
    bookNo,title,author,price
    Develop a menu-driven program( with functions for each) with the following options:
    1:Search Book by author
    2:Search Books below specified price (Rise an exception if price entered is <=0
    3:Search Books where tilte contains the specified word
    4:Exit
'''
import csv
# fields=['bookNo','title','author','price']
with open("books.csv",'w',newline="") as file:
    writer = csv.writer(file)
    count=int(input("Enter the number of books: "))
    # writer.writerow(fields)
    data=[]
    for i in range(count):
        li=[]
        print("enter details for item ",i+1)
        li.append(i+1)
        li.append(input("Enter book title: "))
        li.append(input("author name: "))
        li.append(int(input("Enter Price: ")))
        data.append(li)
    print(data)
    writer.writerows(data)

def search_by_author(value):
    with open("books.csv", "r") as file:
        reader = csv.reader(file)
        for a in reader:
            if a[2].lower() == value.lower():
                return a
        return []

def search_by_price(value):
    with open("books.csv", "r") as file:
        reader = csv.reader(file)
        li=[]
        for a in reader:
            if int(a[3]) < value:
                li.append(a)
        return li

def search_by_word(value):
    with open("books.csv", "r") as file:
        reader = csv.reader(file)
        li=[]
        for a in reader:
            if value in a[1].split():
                li.append(a)
        return li

print("1:Search Book by author\n2:Search Books below specified price (Rise an exception if price entered is <=0\n3:Search Books where tilte contains the specified word\n4:Exit")
while True:
    val=int(input("enter choice: "))
    if val == 1:
        value = input("Enter books author: ")
        print("book is: ",search_by_author(value))
    elif val==2:
        value=int(input("enter price: "))
        print("books are: \n",search_by_price(value))
    elif val==3:
        value = input("enter word: ")
        print("books are: \n",search_by_word(value))
    else:
        print("Bye!!")
        exit(0)



