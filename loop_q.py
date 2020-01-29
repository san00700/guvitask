a = []
print(' Enter the letters in the list ')
while (True):
    n = str(input('please enter any letter : '))
    print(n)
    if (n == 'q' or n == 'Q') :
      print ('invalid value')
      break;
    a.append(n)
    print('valid value')      
print (a)
