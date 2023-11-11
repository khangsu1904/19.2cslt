years=int(input('Enter human years: '))
if 2>=years>0:
    dog=years*10.5
    print(f'{years} human years are {dog:.0f} dog years')
elif years>2:
    dog=10.5*2+4*(years-2)
    print(f'{years} human years are {dog:.0f} dog years')
else:
    print('Error')

