msg ="we will be seeing the horizon"

words =msg.split()
print(words)

words =msg.split('e')
print(words)
# replace()
updated_msg =msg.replace('seeing','viewing')
print(updated_msg)

updated_msg =msg.replace('e','')
print(updated_msg)

#join()
path =['users','mypc','documents','data','data','file.txt']

content ="/".join(path)
print(content)

#strip()
name =" hello steve   "
cleaned_name =name.strip()
print(cleaned_name)
print(len(name),len(cleaned_name))

msg2 =''' 
we are venom
'''
cleaned_msg2 =msg2.strip()
print(cleaned_msg2)
print(len(msg2),len(cleaned_msg2))

from helper import read
data=read('pride_n_prejudice.txt')
# WAP to find frequency of all the vowels in the 'data'

for vowel in 'aeiou':
    print(f"{vowel} =>{data.lower().count(vowel)}times")

#WAPto remove all the punctuations from the string
#str ='he@11%!@&*(!@wo!@r,1!d)'
from string import punctuation
for p in punctuation:
   str=str.replace(p,'')
   print(str)
    

