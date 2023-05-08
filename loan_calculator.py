import math
import argparse
import sys

INCORRECT_PARAMETERS = "Incorrect parameters"

parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str)
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

if args.type != "annuity" and args.type != "diff":
    print(INCORRECT_PARAMETERS)
    sys.exit()
elif args.type == 'diff' and args.payment is not None and args.payment > 0:
    print(INCORRECT_PARAMETERS)
    sys.exit()
elif args.interest is None:
    print(INCORRECT_PARAMETERS)
    sys.exit()

interest = args.interest
nominal = interest / (12 * 100)

if args.principal is not None and args.payment is not None:
    loan_principal = args.principal
    payment = args.payment
    number_months = math.ceil(math.log(payment / (payment - nominal * loan_principal), 1 + nominal))
    years = math.floor(number_months / 12)
    overpayment = number_months * payment - loan_principal
    if years == 0:
        if number_months > 1:
            print(f"It will take {number_months} months to repay this loan!")
        else:
            print("It will take a month to repay this loan!")
    elif years == 1:
        rest_months = number_months % 12
        if rest_months > 1:
            print(f"It will take a year and {rest_months} months to repay this loan!")
        elif rest_months == 0:
            print("It will take a year to repay this loan!")
        else:
            print("It will take a year and a month to repay this loan!")
    else:
        rest_months = number_months % 12
        if rest_months > 1:
            print(f"It will take {years} years and {rest_months} months to repay this loan!")
        elif rest_months == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and a month to repay this loan!")
elif args.principal is not None and args.periods is not None:
    loan_principal = args.principal
    periods = args.periods
    if args.type == "diff":
        overall = 0
        for month in range(1, periods + 1, 1):
            payment = math.ceil(
                (loan_principal / periods) + nominal * (loan_principal - ((loan_principal * (month - 1)) / periods)))
            overall += payment
            print(f"Month {month}: payment is {payment}")
        overpayment = overall - loan_principal
    else:
        payment = math.ceil(loan_principal * ((nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1)))
        overpayment = periods * payment - loan_principal
        print(f"Your monthly payment = {payment}!")
else:
    payment = args.payment
    periods = args.periods
    loan_principal = round(payment / ((nominal * (1 + nominal) ** periods) / ((1 + nominal) ** periods - 1)))
    overpayment = periods * payment - loan_principal
    print(f"Your loan principal = {loan_principal}!")
print(f"Overpayment = {overpayment}")
