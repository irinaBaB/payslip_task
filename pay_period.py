import datetime
from datetime import date

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
    delta = ''

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
            start_date = date(year_s, month_s, day_s)
            #             print(type(start_date))
            #             new_date =datetime.strptime(start_date, "%d/%m/%y").date()
            #             print(new_date)
            #             new_date =datetime.date(date.replace('-', ',').replace('-',',').replace('-', ' ,'))
            #             print(new_date)
            year_e, month_e, day_e = map(int, end_date.split('/'))
            end_date = date(year_e, month_e, day_e)
            print(end_date)
            if (start_date) >= (end_date):
                print("Start date cannot be more than end end")
                break


#             delta==date.strptime(end_date)-date(start_date):
#                     print(delta.days)

            print(
                f'The start of pay period is : \n{start_date.day} of {start_date.strftime("%B")}'
            )
            print(
                f'The end of pay period is : \n{end_date.day} of {end_date.strftime("%B")}'
            )
        return start_date, end_date

pay_period()