'''
Create a system using Object Composition and Encapsulation concepts that allows customers
to place orders for products.
The program consists of three classes: Customer, Order, and Product.
The Customer class stores the customer&#39;s name, email and a list of their orders. It has methods
to return name and email; place and return orders.
The Order class stores orderID and a list of products and has methods to return orderID and to
calculate total price for an order.
The product class stores the name and price of a product and has methods to return name and
price.
'''
import sys

class Product:
    def __init__(self,name='',price=0.0):
        self._name=name
        self._price=price

    def name(self):
        return self._name

    def price(self):
        return self._price

    def __str__(self):
        return " Name: "+str(self._name)+"\n Price: "+str(self._price)

class Order:
    def __init__(self,orderId=1,products=[]):
        self._orderId=orderId
        self._products=products

    def calculate_price(self):
        cost=0.0
        for a in self._products:
            cost+=a.price()
        return cost

    def orderID(self):
        return self._orderId

    def display_products(self):
        s=""
        for a in self._products:
            s=s + str(a) +'\n'
        s+=" Total price: "+str(round(self.calculate_price(),2))+"\n"
        return s

    def __str__(self):
        return "orderID: "+str(self._orderId)+"\n"+self.display_products()


class Customer:
    order=0
    def __init__(self,name="maggie",email="mkbhat2003@gmail.com",orders=[]):
        self._name=name
        self._email=email
        self.orders=orders

    def email(self):
        return self._email

    def name(self):
        return self._name

    def place_order(self,products=[]):
        self.order+=1
        for i in range(1,len(products)+1):
            print(i,": \n",products[i-1])
        val=list(map(int,input("enter index of all products that u want to order(in single line, example: 2 3 4 ): ").split()))
        selection=[products[i-1] for i in val]
        self.orders.append(Order(self.order,selection))
        print("Order is placed\n")
        print(self.orders[-1])

    def display_orders(self):
        print("Orders: ")
        for a in self.orders:
            print(a)

    def return_order(self):
        val=int(input("Enter orderID: "))
        for i in range(len(self.orders)):
            if self.orders[i].orderID()==val:
                self.orders.pop(i)
                print("Removed successfully")
                break
        else:
            print("Couldnt find the order!!!")

    def __str__(self):
        return "Name: "+self._name+"\nEmail: "+self._email


prod=[Product("maggie",20),Product("Noodles",50),Product("Vadapav",15),Product("Samosa",17)]

cus=Customer()
print('''1)account info
2)add order
3add product
4)return order
5)display orders
6)exit''')
while True:
    val=int(input("Enter your choice: "))
    if val==1:
        print(cus)
    elif val==2:
        cus.place_order(prod)
    elif val==3:
        prod.append(Product(input("Enter name of product: "),float(input("Enter price of the product"))))
    elif val==4:
        cus.return_order()
    elif val==5:
        cus.display_orders()
    elif val==6:
        sys.exit()
    else:
        print("Incorrect choice!!")






