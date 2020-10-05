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

    while start_date == '' and end_date == '':
        start_date = input('Enter start date in format yyyy/mm/dd : ')
        end_date = input('Enter end date in format yyyy/mm/dd : ')
        if start_date == '':
            print('You did not entered start date')
            break
        if end_date == '':
            print('You did not entered end date')
            break
        else:
            year_s, month_s, day_s = map(int, start_date.split('/'))
            x = datetime.datetime(year_s, month_s, day_s)
            year_e, month_e, day_e = map(int, end_date.split('/'))
            y = datetime.datetime(year_e, month_e, day_e)

            print(
                f'The start of pay period is : \n{x.day} of {x.strftime("%B")}'
            )
            print(
                f'The end of pay period is : \n{y.day} of {y.strftime("%B")}')
        return x, y


pay_period()