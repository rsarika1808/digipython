#Python 3 code to demonstrate
#Maximum frequency character in string 
#naive method

#initializing string
from tkinter import E


test_str = input("Enter a string:- ")
#printing original string
print("The original string is:"+ test_str)
#using naive method to get
#Maximum frequency character in string
all_freq ={}
for i in test_str:
  if  i in all_freq:
    all_freq [i] +=1  
else:all_freq[i] =1
res = max(all_freq, key = all_freq.get)
#printing result("The maximum of all characters in GeeksforGeeks is:" +str{res aa })
print("result" , res)

