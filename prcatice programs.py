

   examples:
term=int(input("enter the term"))
if term%3==0:
    term=term//3
    print(4**(term-1))
else:
    term=term//3+1
    print(3**(term-1))

num=[2,3,4,34]
num.append(0)
print(num)


def happy_number(n):
    if n == 1:
        return True
    sum,x=n,n
    while sum >25:
        sum=0
        while x >0:
            d=x%26
            sum +=d*d
            x = int (x/26)
        if sum ==1:
            return True
        x = sum
n=int(input("enter a number:"))
if happy_number(n):
    print("it is happy number:", n)
else:
    print("it is not a happy number:",n)

def outf():
    var=30
    def innf():
        var=40
        print("inner var",var)
    innf()
    print("outer var",var)
outf ()


#write a program with a user defined function which returns an integer value to the caller

def cube(x):
    return(x*x*x)
num= 30
result = cube (num)
print("output of the evaluation is",result)

output of the evaluation is 27000
     




















