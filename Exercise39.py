Decibels = float(input('The number of decibels: '))
if Decibels > 0 and Decibels < 40:
    print('Quiet room')
elif Decibels == 40:
    print('Quiet room')
elif Decibels > 40 and Decibels < 70:
    print('between a Quiet room and an Alarm clock')
elif Decibels == 70:
    print('Alarm clock')
elif Decibels > 70 and Decibels < 106:
    print('between an Alarm clock and a Gas lawnmover')
elif Decibels == 106:
    print('Gas lawnmower')
elif Decibels > 106 and Decibels < 130:
    print('between a Gas lawnmover and a Jackhammer')
elif Decibels == 130:
    print('Jackhammer')	
elif Decibels > 130:
    print('Way too loud')
else:
    print('Please enter a correct data value')
    print('Your sound level is')