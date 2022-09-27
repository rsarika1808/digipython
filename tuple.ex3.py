#tuple-set -list (interchangeable)

from telnetlib import XAUTH


x =[1,2,3,4,5,5,6,6,7]
xt =tuple(x) #list ->tuple
x1 =list(xt) #tuple-> list
xs =set(x) #list ->set
x1 =list(xs) #set ->list
xs =set(xt) #tuple -> set
xt =tuple(xs) #set -> tuple
print(x)
print(xt)
print(x1)
print(xs)
print(xt)
#wap to create a tuple, by taking ten input from the user



    


