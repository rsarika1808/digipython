salary=int(input("enter ur salary"))
if salary> 100000:
    print("da=3.5 % hra9.1%")
    da=(salary*3.5)/100
    hra=(salary*9.1)/100
    print("final salary",salary-da-hra)
elif salary>80000:
    print(" da3.2% hra 9%")
    da=(salary*3.2)/100
    hra=(salary*9)/100
    print("final salary",salary-da-hra)
elif salary>60000:
    print("da2.8% hra9%")
    da=(salary*2.8)/100
    hra=(salary*9)/100
    print("final salary",salary-da-hra)
elif salary>50000:
    print("da2.5% hra8%")
    da=(salary*2.5)/100
    hra=(salary*8)/100
    print("final salary",salary-da-hra)
elif salary>40000:
    print("da2.5% hra7.7%") 
    da=(salary*2.5)/100
    hra=(salary*7.7)/100
    print("final salary",salary-da-hra)
elif salary>30000:
    print("da2.2% hra 8%")
    da=(salary*2.2)/100
    hra=(salary*8)/100
    print("final salary",salary-da-hra)
elif salary>20000:
    print("da2.2% hra 7%")
    da=(salary*2.2)/100
    hra=(salary*7)/100
    print("final salary",salary-da-hra)
elif salary>10000:
    print("da2.2% hra 6%") 
    da=(salary*2.2)/100 
    hra=(salary*6)/100 
    print("final salary",salary-da-hra)