""" This program is written to execute operations of double ended queue until the programer requires"""
print("**DOUBLE ENDED QUEUE**")

class Deque:                                    #creating a class for deque
    def __init__(self):
        self.items = []
    def isempty(self):                         #intially queue is empty
        return self.items == []
    def display(self):
        if(self.isempty()==True):
            return "Nothing"
        else:
            return self.items

    def addrear(self, item):                   #adding elements in the rear(start)
        self.items.append(item)

    def addfront(self, item):                 #adding elements in the end(front)
        self.items.insert(0,item)

    def removefront(self):                    #removing or poping  elements in the front(end)
        return self.items.pop(0)
    def removerear(self):                     #removing elements in the rear(start)
        return self.items.pop()
    def size(self):                            #Size of the queue
        return len(self.items)

d=Deque()                                   #creating a queue blank

print("addfront<value>")
print("addrear<value>")
print("removefront")
print("removerear")
print("display")
print("isempty")
print("size")
print("quit")

while True:                                                           #using do while for further process
    do=input("What would you like to do?").split()
    operation=do[0].strip().lower()                                  #for adding elements we will strip the given input
    if operation=="addfront":
        d.addfront(do[1])
    elif operation=="addrear":
        d.addrear(do[1])
    elif operation == "removefront":
        print(d.removefront(), " removed front element from the double ended queue")
    elif operation == "removerear":
        print(d.removerear(), " removed rear element from the double ended queue")
    elif operation == "display":
        print("The elements in the double ended queue is: ", d.display())
    elif operation == "isempty":
        print("Double ended queue is empty(True or False): ", d.isempty())
    elif operation == "size":
        print("The size of the double ended queue is: ", d.size())
    elif operation == "quit":
        break
"""
Test cases:
**DOUBLE ENDED QUEUE**
addfront<value>
addrear<value>
removefront
removerear
display
isempty
size
quit
What would you like to do?display
The elements in the double ended queue is:  Nothing
What would you like to do?addfront 2
What would you like to do?addrear 4
What would you like to do?display
The elements in the double ended queue is:  ['2', '4']
What would you like to do?size
The size of the double ended queue is:  2
What would you like to do?isempty
Double ended queue is empty(True or False):  False
What would you like to do?removefront
2  removed front element from the double ended queue
What would you like to do?removerear
4  removed rear element from the double ended queue
What would you like to do?size
The size of the double ended queue is:  0
What would you like to do?quit
"""
