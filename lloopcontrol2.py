while True:
    price =int( input('enter pricce of item:'))
    if price <0:
        break
    print(f'you entered {price}amount')

    x =[1,2,3,4,-3,5,6,7,87,89]
    for i in x:
        if i<0:
            break
        print(i)