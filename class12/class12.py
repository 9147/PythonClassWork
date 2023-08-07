'''
    07 August 2023
    OOPS in python
'''

# calling class from another file
from objects import Product
val=Product("demo",10000,5)
print(val.getDiscountPrice())




# simple class example
# class Demo:
#     def __init__(self):
#         self.a = 0
#
#     def __str__(self):
#         return "value of a is: " + str(self.a)
#
#
# a = Demo()
# a.a = int(input("enter a number: "))
# print(a)



# inheritance example
# class Base:
#     def __init__(self,a):
#         self.a=a
#     def __str__(self):
#         return str(self.a)
#
#     def show(self):
#         print("showing")
#
# class demo1(Base):
#     def show(self):
#         print("demo1")
#
# class demo2(Base):
#     def show(self):
#         print("demo2")
#
# class low(demo1,demo2):
#     pass
#
# val=low(12)
# val.show()


