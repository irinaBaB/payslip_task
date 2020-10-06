from datetime import datetime, timedelta
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

        #case when user didn't enter anything
        if start_date == '':
            print('You did not entered start date')
            break
        if end_date == '':
            print('You did not entered end date')
            break
        else:
            year_s, month_s, day_s = map(int, start_date.split('/'))
            start_date = date(year_s, month_s, day_s)
            year_e, month_e, day_e = map(int, end_date.split('/'))
            end_date = date(year_e, month_e, day_e)

            # case if start_date is higher then end_date
            if (start_date) >= (end_date):
                print("Start date cannot be more than end end")
                break

            #case if the start and end date period more than 30 days
            a = datetime.strptime(str(end_date), "%Y-%m-%d")
            b = datetime.strptime(str(start_date), "%Y-%m-%d")
            delta = a - b
            if delta.days > 30:
                print(
                    "Your pay period cannot be more then 30 days. Please enter correct end date"
                )
                break
            #this payslip will be generated only based on start date plus it has fixed date
            print(
                f'Your  payslip will be generated from the  1st of {start_date.strftime("%B")} to 30st of {start_date.strftime("%B")}'
                )
        return start_date, end_date
