# dictionary with integer keys
from signal import valid_signals


my_dict = {1:'apple',2:'ball'}

val =['rajendrasingh',30,4,'accounts','staff officer',600000,7,]

val_dict ={

    'employee':'rajendrasingh','age':30,
    'experience': 10,'dept':'ACCOUNTS',
    'designation':'system officer','salary':600000,
    'team_size':7
}

#displaying a dict
print(val_dict)

#retreival of value
ans =val_dict['designation']#key in sqr brackets
print(ans)
print(val_dict['salary'])#correct
print(val_dict['experience'])#incorrect

#adding a data inside dict
val_dict['company']='acme.inc'
print(val_dict)

from pprint import pp 
pp(val_dict)