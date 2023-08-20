class Product:
    def __init__(self,name='',price=0.0,discount_percentage=0.0):
        self.name=name
        self.price=price
        self.discount_percentage=discount_percentage

    def getDiscountAmount(self):
        return round(self.price * self.discount_percentage /100,2)

    def getDiscountPrice(self):
        return round(self.price - self.getDiscountAmount(),2)

    def __str__(self):
        return f'Name:{self.name}\nPrice:{self.price}\nDiscount percentage{self.price}%\nDiscount amount:{self.getDiscountPrice()}\nDiscount price:{self.getDiscountPrice()}\n'
li=[]
li.append(Product("Stanley 13 Ounce Wood Hammer",12.99,62))
li.append(Product("National Hardware 3/4\" Wire Nails",100,30))
li.append(Product("Economy Duct Yape, 60 yds, Silver",1000,25))

val=True
print("Products:")
for a in li:
    print(a.name)
while val:
    value=int(input("Enter product number: "))
    print(li[value-1])
    temp=input("View another product? (y/n): ")
    val=temp.lower()=='y'

