def payslip_details():
    user_name = False
    surname = False
    start_date = ''
    end_date = ''
    annual_salary = None
    gross_income = None
    rate = None

    while user_name == False and surname == False:
        user_name = input("Please enter your name: ")
        surname = input("Please enter your surname: ")
        if len(user_name) == 0:
            print("Sorry, the name is incorrect, please enter the name")
        elif len(surname) == 0:
            print(
                "Sorry, the surname is incorrect, please enter the correct surname"
            )
        return (user_name.title(), surname.title())

    while start_date == '' and end_date == '':
        start_date = input('Please enter your paymr start date : ')
        end_date = input('Please enter your payment end date : ')
        return start_date,end_date

    while annual_salary == None:
        annual_salary = input("Please enter your annual salary: ")
        return annual_salary

    while annual_salary == None:
        rate = float(input("Please enter your super rate: "))
        return rate