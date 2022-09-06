from nis import match
from socket import CAN_BCM_TX_SETUP


num=int(input('entera number'))
match num:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tuesday')
    case 4:
        print('wednesday')
    case 5:
        print('thursday')
    case 6:
        print('friday')
    case 7:
        print('saturday')
    case: # char act as a default,if none of the cases match
        print('invaild data')
      

