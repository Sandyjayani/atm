
#Check for valid pin.
def verify_pin(pin):
    return pin == 1111

#Give user three attempts to try pin
def log_in():
    tries = 0
    while tries < 3:
        pin =int(input('Please Enter Your 4 Digit Pin: '))
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Could not log in")
    return False


def check_input(withdraw):
    try:
        withdraw = int(withdraw) # check if input is a number
        try:
            if withdraw <= 0: # check if withdraw is negative
                raise ValueError("Please enter a valid amount. ")
        except ValueError as ve:
            print (ve)
            return False
    except ValueError:
        print("Invalid input")
        return False
    else:
        return True


# transaction function to withdraw money
def transaction(withdraw):
    balance = 100 ##set account balance to 100
    try:
        x = balance - withdraw
        if x < 0: # check if balance is negative
            raise ValueError("Insufficient fund!")
    except ValueError as ve:
        print(ve)
    else:
        balance -= withdraw  # subtract withdraw from balance 
        print(f"Your balance is: £{balance}.")
    return balance
def main():
    if log_in():
        withdraw = (input('please enter withdrawal amount: '))
        if check_input(withdraw):
            transaction(int(withdraw))

main()







