import datetime

#assuming we only firmly calculating monthly payslip, only based on start date
#user entered start date ex: 2020/04/03
#user entered end date ex: 2020/07/03
# use delta to calculate number of the days - > if more then 30 - return error -> pay period cannot be more then 30 days
# return pay slip period based on start date

def pay_period():
    start_date = ''
    end_date = ''
    year = ''
    month = ''
    day = ''

    while start_date == '':
        start_date = input('Enter start data in format yyyy/mm/dd : ')
        year, month, day = map(int, start_date.split('/'))
        x = datetime.datetime(year, month, day)

        print(f'The start of pay period is : {x.day} of {x.strftime("%B")}')
    return x.strftime('%A')


pay_period()