'''marks=[15,5,10]
print(marks[-1])
10print(i)


marks=[15,5,10]
for i in range(len(marks)):
    print(i)
    print(i, "=", marks[i])


for i in marks:
    print(i)

0
0 = 15
1
1 = 5
2
2 = 10
15
5
10

marks=[15,5,10]
for i in range(len(marks)):
    for j in range(i+1,len(marks)):
        if(marks[i]>marks[j]):
            marks[i],marks[j]=marks[j],marks[i]
print(marks)

[5, 10, 15]

marks=[15,5,10,-5,25,-5,25,-5]
key=int(input("enter the key:"))
if key in marks:
    print("yes")
else:
    print("no")

marks=[15,5,10,-5,25,-5,25,-5]
l=[]
for i in range(len(marks)):

    c=2
    for j in range(i+1,len(marks)):
        if marks[i]==marks[j]:
            c+=1
            if marks[i] not in 1:
                print(marks[i],"present in the list",c,"times")
                i.append(marks[i])


list=[15,5,10,-5,25,-5,25,-5,100,'d']
count={}
for i in list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

{15: 1, 5: 1, 10: 1, -5: 3, 25: 2, 100: 1, 'd': 1}'''


list=[15,5,10,-5,25,-5,25,-5,100,'d',97,'a']
count={}
for i in list:
    if str(i)==i:
        i=ord(i)
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

'''op:
{15: 1, 5: 1, 10: 1, -5: 3, 25: 2, 100: 2}'''

















































