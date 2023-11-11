print('List of months: January, February, March, April, May, June, July, August, September, October, November, December')
Month_name = input('The name of Month: ')
if Month_name == 'February':
    print('No. of days: 28/29 days')
elif Month_name in ('April', 'June', 'September', 'November'):
    print('No. of days: 30 days')
elif Month_name in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
    print('No. of days: 31 days')
else:
    print('Error month name')