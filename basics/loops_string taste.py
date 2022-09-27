# defining strings in python
# all of the following are equivalent
from colorsys import ONE_THIRD
from curses.ascii import isupper
from itertools import count
from pickletools import string1
from random import Random
import string
from tabnanny import check
from xml.etree.ElementInclude import include

from macpath import split


my_string ="hello"
print(my_string)

my_string ='hello'
print(my_string)

my_string ='''hello'''
print(my_string)

#triple quotes string can extend multiple lines
my_string="""hello, welcome to 
          theworld of python"""

print(my_string)

#2 str 
def string_length(str):
    count=0
    for char in string1:
        count+=1
        return count
    print(string_length('python'))

#3
#function which returns last word 
def lastword(string):
    #taking empty string 
    newstring =""

    #calculating length of string
    length =len(string)

    #traversing from last
    for i in range(length -1,0,-1):
        #if sapce is occurred then return
        if(string[i]==""):
    #return reverse of newstring
         return newstring[::-1]
    else:
        newstring =newstring +string
    #driver code
    string ="learn algorithms at geekforgeeks"
    print(lastword(string))

#4
word="they stumble who run fast"
space =word.count('')
start =0
while space !=-1:
    print(word[start:space])

#5

def reverse(s):
    str =""
    for i in s:
        str =i+str
        return str
        s="hello world"
        print("the original string is:",end="")
        print(s)
        print("the reversed string(using loops) is:",end ="")
        print(reverse(s))

#6

#example string
string ="how are you?"
print(string.upper())

#string with number
#all alphabets should be lowercase
string ="where are from?"
print(string.upper())

#7
#example string
string ="How Is It Going?"
print(string.lower())

#string with numbers
#all alphabets should be lowercase
string ="How Is It going2?  "
print(string.lower())

#8

#python program to print list

a=['pyhton','is','easy']
#printing the list using *and sep operator
#by sapce

print(*a)

#printing the list using * and sep operator
print("printing lists separted by commas")

print(*a,sep =",")
#print in new lines

print("printing lists in new line")

print(*a,sep ="\ n")

#9

my_string ='''The only way
 to learn to program is
 by writing code '''

print(my_string)

#10
print("line1{n1}")
print ("line2 {n2}")
print ("line3".format(n1="\ n"))
n1 ="\n"
print(f"line1{n1}")
print(f"line2{n1}")
print("line3")


#11

#how tp print a string
print("hollo world")

#how to print an integer
print(15)
#how to print a variable 
# to just print the variable in its


fave_language ="python"
print(fave_language)


#12

s ='Python'+'Is'+'Great'
print(s)
#PythonIsGreat
s1='Python'
s2='Is'
s3='Great'
s =s1+s2+s3
print(s)
#pythonIsGreat
s=s1+s2+s3+'ddd'
print(s)
#PyhtonIsGreat

#13

print name(n):
if(n>0):
    printName(n-1)
    print(n,"My Name")
    printName(13)


#14
for i in range(1,9+1):
    print(i,".")

#15

def convert(1st)
return([i for i in Ist.split()])
#drivercode
Ist ="Geekforgeeks"is a pertal for geeks"
print(convert(Ist))

#16

print(mystr.endswith('.'))#returns True
print(mystr.endswith('age'))#returns True
print(mystr.endswith('language'))#returns True
print(mystr.endswith('programming language'))#returns True
print(mystr.endswith('age'))#returs False,is missing

#17

inp =input("STATEMENT")
>>>name =input('what isyour name?\n')#\n--->new line
>>>what is your name?
Ram 
>>>print(name)
Ram 
#---->comment in python


#18
a ="\u0030" #unicode for 0
b ="\u00B2" #unicode for &sup2
c ="10km2"
d ="-1"
e ="1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

#19
my_string ="text"
my_string =my_str.strip()

#20

an_pper ="A"
An_uppercase_check=an-upper.isupper()
print can_uppercase-check
a-lower ="a"
onother_uppercase_check =a_lower.isupper()
print(another_uppercase_check)

#21
#Python3 code do demonstrate
#to extract words from string
#using split()
#initalizing string
text_string ="Joe,david,mark, tom,c"
#printing original. string
print("The original.string is:"+test_string)
#using split()
#to extract words string
res =test_string.split
#printing result.
print("The list of wordis:"+str(res))

#22
def add_string(str1):
    length =len(str1)
    if length >2:
        if str1[-3:]=="ing":
            str1+ ='ly'
            else:
        returne string1
        print(add_string('ab'))
        print(add_string('abc'))
        print(add_string('string'))

#23
str ="hello, word!"
if str.find ("world")! =1:
    print("found the string")
else:
    print("Not found!!!")

#24

#Remove special characters from a string using re.sub()
import re.sub(r"[^a-ZA-Zo-9],text")

print(new_text)

#25
text =input ()
length_word =0
total_word =0
words = text.split()
for.X in words:
    length_words +=1
    average =length_words/total_word_words
    print(average)
    words= input()
    























