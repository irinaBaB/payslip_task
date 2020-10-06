range1 = range(0, 18201)
range2 = range(18201, 37001)
range3 = range(37001, 87001)
range4 = range(87001, 180001)



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


def income_tax(gross_salary, income_tax=0):
    if gross_salary in range1:
        #Nil tax
        income_tax = 0
    elif gross_salary in (range2):
        #19c for each $1 over $18200
        income_tax = round(((gross_salary - 18200) * 0.19) / 12, 2)
    elif gross_salary in range3:
        #$3572 plus 32.5c for each $1 over $87000
        income_tax = round((3572 + (gross_salary - 37000) * 0.325) / 12, 2)
    elif gross_salary in range4:
        #$19822 plus 37c for each $1 over $87000
        income_tax = round((19872 + (gross_salary - 87000) * 0.37) / 12, 2)
    elif gross_salary >= 180001:
        # $54232 plus 45c for each $1 over $180000
        income_tax = round((54232 + (gross_salary - 180000) * 0.45) / 12, 2)

    return income_tax