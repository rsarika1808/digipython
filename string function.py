
from helper import read
data =read('pride_n_prejudice.txt')
print(len(data))

newdata = data [3:70]
print(newdata)


'''
formatting functions
-lower
-uper
-swapcase
-capitalize
-title
-ijust
-rjust
-casefold
-center
'''
print('lower =>',newdata.lower())
print('upper =>',newdata.upper())
print('swapcase =>',newdata.swapcase())
print('capitalize =>',newdata.capitalize())
print('title =>',newdata.title())
print('casefold =>',newdata.casefold())


word ='Hello'
spacing =20

Ijust=word.Ijust(spacing,'*')
print(Ijust)

rjust =word.rjust(spacing,'"')
print(rjust)

cen =word.center(spacing,'-')
print(cen)


#vaildation function -either true or false
print(newdata.isupper())
print(newdata.islower())
print(newdata.isalpha())
print(newdata.isnumeric())
print(newdata.isalnum())

#utility function
idx =newdata.find("Pride")
if idx==-1:
    print('not found')
else:
    print (f'Pride was found at index.{idx}')

idx2 =data.index("in")
print(f'in was found at index{idx}')

start_idx=0
for i in range(5):
    idx3=data.find('in',start_idx)
    print(f'in was found at{idx3}')
    start_idx=idx3+1

num_of_in =data.count('in')
print(f'in occurs{num_of_in}times')












