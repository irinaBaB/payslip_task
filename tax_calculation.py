def gross_income():
    annual_salary = None
    gross_salary = None

    while annual_salary == None:
        annual_salary = input("Please enter your annual salary: ")

        if annual_salary.isdigit() == False:
            print(
                'You have not entered the correct format of the value, try again'
            )
            break
        if annual_salary.isdigit() == True:
            gross_salary = round(int(annual_salary) / 12, 2)
            print(gross_salary)
    return int(gross_salary)