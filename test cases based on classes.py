'''#write a program to check the given number is even or odd by using single stance class object with an attribute following a constructor
#test case 21
class number:
    even=0
    def check(self,num):
        if  num%2==0:
             self.even= 1
    def even_odd(self,num):
            self.check(num)
            if self.even==1:
                print(num, "is even")
            else:
                print(num, "is odd")
n= number()
n.even_odd(21)

output:
21 is odd


class number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num= num
        if num%2 ==0:
            number.even.append(num)
        else:
            number.odd.append(num)
n1= number(11)
n2= number(12)
n3= number(13)
n4= number(28)
n5= number(7)
print ("even number list is ",number.even)
print ("odd number list is ",number.odd)

output:
even number list is  [12, 28]
odd number list is  [11, 13, 7]


write a program that has a class named circle use a class variable to define the values of constant pi.use this class variable to caluclate area and circumference of the circle with specified radius where radius=7.5?''
class circle:
    pi=3.14159
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.pi*self.r*self.r
    def circum(self):
        return 2*circle.pi*self.r
c=circle(7.5)
print("area=",c.area())
print("circumference=",c.circum())

output:
area= 176.7144375
circumference= 47.12385'''
















        
