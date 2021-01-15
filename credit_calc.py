import math
import argparse

my_parser = argparse.ArgumentParser(description='It is my Loan Calc script')
my_parser.add_argument('--type', '-t', choices=['annuity', 'diff'], required=True, help='Type "diff" for differentiate \
 payments calculation or "annuity" for equal payments calculation')
my_parser.add_argument('--principal', '-l', type=int, help='Type here loan principal')
my_parser.add_argument('--payment', '-p', type=int, help='Value of monthly payment')
my_parser.add_argument('--interest', '-i', type=float, help='Type here annual interest rate')
my_parser.add_argument('--periods', '-m', type=int, help='Type here number of periods for annuity calculations')

args = my_parser.parse_args()


def diff_calc():  # differentiated: interests, principal, periods
    overpayment = 0
    int_rate_mont = (args.interest / 12) / 100

    for m in range(1, args.periods + 1):
        differ = math.ceil((args.principal / args.periods) + int_rate_mont * (args.principal - ((args.principal * (m - 1)) / args.periods)))
        overpayment += differ
        print(f'Month {m}: payment is {differ}')

    result_overpay = overpayment - args.principal
    print(f' overpayment = {result_overpay}')


def annuity_calc():  # annuity: interests, principal, periods
    i = args.interest / 100 / 12
    annuity = args.principal * ((i * pow((1 + i), args.periods)) / (pow((1 + i), args.periods) - 1))
    overpayment = math.ceil(annuity) * args.periods - args.principal
    print(f'Your annuity payment = {math.ceil(annuity)}!')
    print(f'Overpayment = {overpayment}')


def loan_principal_calc():  # annuity: payment, periods, interests
    interest_rate_monthly = (args.interest / 12) / 100
    result = (args.payment / ((interest_rate_monthly * math.pow(
        (1 + interest_rate_monthly), args.periods)) / ((math.pow((1 + interest_rate_monthly), args.periods)) - 1)))
    overpayment = (args.periods * args.payment) - result
    print(f'Your loan principal = {math.ceil(result)}! \n Overpayment = {math.ceil(overpayment)}')


def number_of_months_calc():  # annuity: principal, payment, interests
    interest_rate_monthly = (args.interest / 12) / 100
    number_of_months = math.ceil(math.log((args.payment / (args.payment - (
                interest_rate_monthly * args.principal))), interest_rate_monthly + 1))
    overpayment = (args.payment * number_of_months) - args.principal

    if number_of_months % 12 == 0:
        print(f'It will take {int(number_of_months) // 12} years to repay '
              f'the loan \n Overpayment = {overpayment}')
    else:
        print(f'It will take {int(number_of_months) // 12} years and '
              f'{int(number_of_months) % 12} months \n Overpayment = {overpayment}')


if args.interest is None or args.interest == 0.00:
    print('Incorrect parameters')
else:
    if args.type == 'annuity' and args.payment is None:
        annuity_calc()
    elif args.type == 'diff' and args.payment is None:
        diff_calc()
    elif args.type == 'annuity' and args.principal is None:
        loan_principal_calc()
    elif args.type == 'annuity' and args.periods is None:
        number_of_months_calc()
