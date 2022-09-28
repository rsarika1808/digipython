from signal import signal


def get_salary():
    val =int(input("ENTER SALARY"))
    fine =.09
    return val*fine

print("salary",get_salary())

a =get_salary() 
print('salary',a)

final_salary =get_salary() +1000 
print('salary',final_salary)

def amount():
    #p =
    #r =
    #t =
    #si
    #omt
    return 0
    
def amount():
    p=int(input('principal:'))
    r =float(input('rate:'))
    t =int(input('Time:'))
    si =p*r*t//100
    amt=si+p
    return amt,si
ans =amount()
print(f'the Amount will be{amount}on simple interest{signal}')
#or this way
print(f'the Amount will be{amount()[0]}')


def word_count(msg):
    words =msg.split()
    return len (words)
word_count("this is time to go")

