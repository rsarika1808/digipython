for i in range(100):
    print('HII',i)
    print(i,end=',')
    
#start stop
    for i in range(10,21):
        print(i,end='x')
# step/gap value
        for i in range(1,11,2):
            print(i,end='0')

# reverse loop

for i in range(10,0,-1):
    print(i,end='')


data=['2,2,4,6,4,3,,1,2,2,3,5']
for i,d in enumerate(data):
    print(i,d)

data=['apple','cherry','gauva','banana','samosa']
for i in enumerate(data):
    print(i,d)

    names=['Apple','Banana','cherry']
    price=[100,40,65]

for n,p in zip(names,price):
    print(f'{n}=>${p}')
