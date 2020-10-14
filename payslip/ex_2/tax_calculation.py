range1 = range(0, 18201)
range2 = range(18201, 37001)
range3 = range(37001, 87001)
range4 = range(87001, 180001)



def gross_income(annual_salary):
    gross_income = round(int(annual_salary) / 12)
    return int(gross_income), int(annual_salary)


def income_tax(annual_salary, income_tax=0):

    if annual_salary in range1:
        #Nil tax
        income_tax = 0
    elif annual_salary in range2:
        #19c for each $1 over $18200
        income_tax = round(((annual_salary - 18200) * 0.19) / 12, 2)
    elif annual_salary in range3:
        #$3572 plus 32.5c for each $1 over $87000
        income_tax = round((3572 + (annual_salary - 37000) * 0.325) / 12, 2)
    elif annual_salary in range4:
        #$19822 plus 37c for each $1 over $87000
        income_tax = round((19872 + (annual_salary - 87000) * 0.37) / 12, 2)
    elif annual_salary >= 180001:
        # $54232 plus 45c for each $1 over $180000
        income_tax = round((54232 + (annual_salary - 180000) * 0.45) / 12, 2)

    return income_tax


def net_income(gross_income, income_tax, net_income=0):
    net_income = gross_income - income_tax
    return net_income


def super_k(gross_income, rate=0):
    return (round(gross_income * (rate / 100)))
