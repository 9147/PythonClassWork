'''
    Date:11 august 2023
'''
##method hiding
# class Demo():
#     def __init__(self):
#         self.val=12
#         self.__val=14
#     def do(self):
#         return self.__val
#
# a=Demo()
# print(a.val)
# print(a.__val)  #this will throw an error

# print(False if 5 in range(2,4) else True)

#read about annotations
#read about data class

#inheritance

class Product:
    def __init__(self,name="",price=0.0,discount=5):
        self.price=price
        self.name=name
        self.discount=discount
