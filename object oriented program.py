'''#program to create and access an obj
class abc:
    var=10
obj=abc()
print(obj.var)

output:10

# program to create self arg and access an obj
class xyz:
     var=100
class abc:
    attribute1=10
    def displat(self):
        print("this is in class method")
obj=abc()
print(obj.attribute1)
obj.displat()

output:10
this is in class method

# program to create to check the constructor
class abc:
    def __init__(self,value):
      print("this is in class")
      self.value=value
      print("the value is",value)
obj=abc(100)

output:
this is in class
the value is 100

#
class abc:
    class_var=0
    def __init__(self,var):
        abc.class_var +=1
        self.var= var
        print("the obj value is ",var)
        print("the class value is ",abc.class_var)
obj1=abc(100)
obj2=abc(101)
obj3=abc(102)

output:
the obj value is  100
the class value is  1
the obj value is  101
the class value is  2
the obj value is  102
the class value is  3'''
    






        
                
