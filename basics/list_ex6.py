import math

x =[2,2,3,3,1,2,3,4,5,6]
print("SUM=>",sum(x))
print("MEAN=>",sum(x)/len(x))
x.short()
if len (x)% 2 ==0:
    idx =len(x)//2
    value =x[idx]+x[idx+1]
    print("median =>",value/2)
else:
    value=x[len(x)//2+1]
    print("median=>",value/2)


#2
names =[]
for i in rang(5):
    names.append(input("name=>"))
    for name in names:
        print(name[::-1])

#3
fib =[0,10]
for i in range(15):
    fib.append(fib[-1]+fib[-2])
    print(fib)

#4 squares
x =[1,2,3,4,5,6,7]
x2 =[]
for num in x:
    x2.append(num ** 2)
    print(x)
    print(x2)

#5 odd values from list
x =[1,2,3,3,4,5,6,7]
xodd =[]
for i in x:
    if i % 2  !=0:
     print(xodd)

#6 add 2 list elementwise
x =[1,2,3,4,5,6]
y =[6,4,3,2,1,2]
z =[]

for i,j in zip(x,y):
    z.append(i+j)
    print(x)
    print(y)
    print(z)
     
for i in range (1,11):
    print(f'2*{i}={2*i}')
    




