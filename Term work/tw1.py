'''
    Develop a menu driven program to implement a queue. THe operation would be
    a.Add an item to the queue
    b.Delete an item from queue
    c.Display the queue
'''

li=[]
val=1
print("1->.Add an item to the queue\n2->.Delete an item from queue\n3->.Display the queue\n4->exit")
while val!=4:
    val=int(input("Select one option: "))
    if val==1:
        a=input("enter a value to add: ")
        li.append(a)
    elif val==2:
        print("the value ",li.pop(0)," is removed")
    elif val==3:
        print("Queue: ",*li)

