humanY = int ( input('Human Years: '))
if humanY < 0: 
    print('Please retype a positive number.')
else:
    if humanY <= 2:
        dogY= humanY*10.5
    else:
        dogY = (2*10.5) + ((humanY -2)*4)
    print (humanY,'human years is equal to',dogY,'dog years')