x =[1,2,3,1,2,3,3,1,1,3,3,1,1,1,2,3,3,1,4,1,1,2,2,2]

x_one = x.count(1)
x_two = x.count(2)
x_four =x.count(4)
x_five = x.count(5)
print('1 occurrred',x_one,'times')
print('2 occurred',x_two ,'times')
print('4 occurred',x_four,'times')
print('5 occurred',x_five,'times')

y =[23,45,6,2,21,22,32,23]
z =[1,3,3,5,6,1]

print('xaddind y')
x.extend(y)
print(x)
print('x adding z')
x.extend(z)
print(x)

xyz =x + y+ z
print(xyz)

a =['apple', 'banana','cherry', 'dragonfruit',]
v =a.pop(3) # pop can remove value from an index
print(a)
print(v)
v=a.pop()#pop removes last value by d
print(a)
print(v)




