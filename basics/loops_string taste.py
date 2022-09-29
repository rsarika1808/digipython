# ques. no1
str ="Hii"
print(str)

#ques.no 2
str =input("Enter a string")
print(len(str))

#ques.no3
str ="python is great"
st =str[-5:]
print(st)
for i in range((len(str)-1),0-1):
    if str[i]=="":
        print(st[::-1])
else:
     st =st+st[i]

# ques.no4
str ='python is everywhere'
print(*str.split(),sep='\n')

#ques no 5

str ='hello world'
s =""
for i in str:
    s= i+s
    print(s)

# ques.no6
str ="how are you"
print(str.upper())

# ques.no7
str ="how is It going?"
print(str.lower())

#ques,no8
words =['python','is','esay','to','lrarn']
print("".join(words))

#ques.no 9

print("print multiline string\ using single print")
#or 
data =""
while True:
    line =input()
    if not line:
        data+=line+'\n'
        print(len(data),'chars')

#ques.no10
print("\\n")
print(r'\n')

#ques.no11
print("The variable is",())

#ques.no12

s1 ='python'
s2 ='is'
s3 ='great'
s =s1+s2+s3
print()

#ques.no13
b='#'
print(b*20)

#ques.no14
for i in range (1,10):
    print( "5")

#ques.no15
sentence =input("enter the sentence:")
print("sentence.split(),sep'\n")

#ques.no16

if sentence[len(sentence)-1]=='?':
    print("The enter of string has '? in the end of the string")
else:
    print("The entered sentence  does not have'?' in it.")
#ques.no17
print(sentence .count('e'))

#ques.no18

print(sentence.innumeric(i))

#ques.no19
text ="This is not a good string"
sen =text.Istrip()
print(sen.rstrip())

#ques.no20
for i in sentence:
    if i. isupper():
        print("Found")

 #ques.no21
names ='Joe,David,Mark,Tom,Chris,Robert'
i=[]
i =names.split(',')
print(i)

#ques.no22
text ='this is some text'
a =text.split()
a.insert(1,'aye')
a.insert(3,'aye')
a.insert(5,'aye')
a.insert(7,'aye')
print(a)

#ques.no23

str =input("enter string to check the 'fyi in the string")
if"fyi" in str:
    print("yes,entered string have'fyi' in the string")
else:
    print("No, entered string does not have 'fyi' in the string")

#ques.no24
text ='%p34@y!*_*!t68h#on404'
from pickletools import string1
from string import punctuation
for p in punctuation:
    text =text. replace(p,'')
    print(text)

#ques.no25
str="this is a paragraph which is weitten just for the purpose of providing content to let the average word length be calculated"
w =string1.split()
print("number of words in the given string is",len(w))

        
    























