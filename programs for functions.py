'''from time import*
t1= perf_counter()
i=sum=0
while i<1000000:
    sum+=i
    i+=1
sleep(0)
t2=perf_counter()
print('execution time=% seconds' %(t2-t1))

output:
execution time=0.13684239995200187econ



def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,b,a,c)
        if a:
            c.append(a,pop())
        hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")

output:
before puzzle'''


'''from datetime import *
d= date.today()
print(d)
d= date(2023,2,3)
for a in range(1,10):
    nextdate = d +timedelta(days=a)'''


'''import math
number=int(input("enter the number to check krishnamurthy number="))
n=number
sum=0
while n>0:
    fact=1
    rem=n%10
    fact=math.factorial(rem)
    sum=sum+fact
    n=n//10
if sum==number:
    print("it is krishnamurthy number",number)
else:
    print("it is not krishnamurthy number",number)'''












































