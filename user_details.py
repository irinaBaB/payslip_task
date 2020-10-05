
print ('Welcome to the payslip generator')

# Input details: (
# name,
# surname,
# annual salary,
# super
# rate,
# payment start date,
# payment end date)


#Calculate:
# pay period (based on entered date  01 March - 31 March (year?))
# gross income
# income tax
# net income
# super

# assumption (no prorata)
# if I enter 31 of March - as start date = 1-31 of March


def user_details():
    user_name = False
    surname = False
    while user_name == False and surname == False:
        user_name = input("Please enter your name: ")
        surname = input("PLease enter the surname: ")
        if len(user_name) == 0:
            print("Sorry, the name is incorrect, please enter the name")
        elif len(surname) == 0:
            print(
                "Sorry, the surname is incorrect, please enter the correct surname")
        print(f'Name: {user_name.title()} {surname.title()}')
        return (user_name.title(), surname.title())


user_details()

