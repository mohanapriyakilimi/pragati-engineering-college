'''class SRMQueue:

    def __init__(shiva):
        shiva.queue = list()
    def add_element(shiva,val):
        if val not in shiva.queue:
            shiva.queue.append(val)
            return True
        return False
    def size(shiva):
        return len(shiva.queue)
    def display(shiva):
        print(shiva.queue)


q1=SRMQueue()
q1.add_element("diwali")
q1.add_element("dhasara")
q1.add_element("x-mass")
q1.add_element("bakreeth")

q1.display()

['bakreeth', 'x-mass', 'dhasara', 'diwali']
        
['diwali', 'dhasara', 'x-mass', 'bakreeth']


class SRMQueue:

    def __init__(shiva):
        shiva.queue = list()
    def add_element(shiva,val):
        if val not in shiva.queue:
            shiva.queue.append('val')
            return True
        return False
    def size(shiva):
        return len(shiva.queue)
    def display(shiva):
        print(shiva.queue)
    def delete_element(shiva,val):
        if val in shiva.queue:
            shiva.queue:pop(0,val)
            print("popped items: "+ shiva.queue.pop(0))
            return True
        return False



q1=SRMQueue()
q1.add_element("diwali")
q1.add_element("dhasara")
q1.add_element("x-mass")
q1.add_element("bakreeth")

q1.display()

q1.delete_element()
q1.delete_element()
q1.delete_element()
q1.delete_element()

q1.display()'''

'''# deque implementation in python

class deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self,item):
        self.items.append(item)

    def addFront(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()'''


a=[1,2,5,3,10]
for i in range(len(a)+1):
    if(a[i]%5==0):
        a.insert(i+1,7)
print(a)










































                 

    





    







































