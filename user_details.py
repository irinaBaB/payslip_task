
print ('Welcome to the payslip generator')


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


