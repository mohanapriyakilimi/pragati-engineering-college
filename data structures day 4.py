'''# binary tree in python




class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

#traverse preorder
    def traversepreorder(self):
        print(self.val,end='')
        if self.left:
            self.left.traversepreorder()

        if self.right:
            self.right.traversepreorder()
    
    def traverseinorder(self):
        if self.left:
            self.left.traverseinorder()
        print(self.val,end='')

        if self.right:
            self.right.traverseinorder()

    def traversepostorder(self):
        if self.left:
            self.left.traversepostorder()

        if self.right:
            self.right.traversepostorder()
        print(self.val,end='')

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.right.right = Node(50)
root.right.right.left = Node(60)
root.right.left = Node(70)
root.right.left.right = Node(80)
root.right.left.right.right = Node(90)
root.right.right.left.right = Node(100)

print("pre order traversal: ",end="")
root.traversepreorder()
print("\nin order traversal: ",end="")
root.traverseinorder()
print("\npost order traversal: ",end="")
root.traversepostorder()
op:
pre order traversal: 12437080905060100
in order traversal: 42170809036010050
post order traversal: 42908070100605031'''


class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

#traverse preorder
    def traversepreorder(self):
        print(self.val,end='')
        if self.left:
            self.left.traversepreorder()

        if self.right:
            self.right.traversepreorder()
    
    def traverseinorder(self):
        if self.left:
            self.left.traverseinorder()
        print(self.val,end='')

        if self.right:
            self.right.traverseinorder()

    def traversepostorder(self):
        if self.left:
            self.left.traversepostorder()

        if self.right:
            self.right.traversepostorder()
        print(self.val,end='')

root = Node("apple")

root.left = Node("banana")
root.right = Node('c')

root.right.right = Node("z ")
root.right.left = Node(" ")

print("pre order traversal: ",end="")
root.traversepreorder()
print("\nin order traversal: ",end="")
root.traverseinorder()
print("\npost order traversal: ",end="")
root.traversepostorder()








































