# defining strings in python
#all of the following are equivlent
my_string ='hello'
print(my_string)
my_string ="hello"
print(my_string)
my_string ='''hello'''
print(my_string)
#string quotes string can extend multiple lines
my_string ="hello,welcome to python"
print(my_string)



a ='Excallibur'
print(a)

b ="smallfoot"
print(b)

c ='''once upon 
a time ,there was a person that used to sleep.
The end'''
print(c)

print(a[0])#first char
print(a[2])#third char
print(a[-1])#last char
print(a[-3])#third last char
print(a[0],a[2])

name ='vijay deenanath chauhan'
for i,c in enumerate(name):
    print(i,c)
mname =name [6:-8]
print(mname)
print(name[6:-8])

fname =name [:5]
print(fname)
iname = name [-7:]
print(iname)
sname = name [11:-8]
print(sname)

# reverse the string
print(name[:: -1])

print(name[:5][:: -1])

# every even idx char
print(name[::2])#vjy

#every odd idx char
print(name[1::2])


x =chr(65)
print(x)
x = chr(2365)
print(x)
x =chr(12365)
print(x)

for i in range(15000,20000):
    print(i,chr(i))

y =ord('A')
print(y)
y = ord('a')
print(y)
y =ord ('{')
print(y)


a ='apple'
b ='juice'
ab =a+b
print(ab)

w1 ='this'
w2 ='is'
w3 ='Amazing'
msg =w1 +w2 +w3
print(msg)
msg =w1 +' '+w2 +' '+ w3
print(msg)

word ='Hii'
print(word * 3)

print('-' * 25)











        
        