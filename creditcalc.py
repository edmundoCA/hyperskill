import math
import argparse

principal = None  # loan principal (P)
payment = None  # monthly payment (A)
months = None  # number of monthly payments (n)
interest = None  # loan interest (i)
type_of_payment = None  # annuity or differentiated
Dm_sum = None
overpayment = None


def calculate_loan_principal():
    global principal
    principal = math.floor(payment / ((interest * math.pow((1 + interest), months)) /
                                      (math.pow((1 + interest), months) - 1)))
    print(f"Your loan principal = {principal}!")


def calculate_monthly_payment():
    global payment
    payment = math.ceil(principal * ((interest * math.pow((1 + interest), months))
                                     / (math.pow((1 + interest), months) - 1)))
    print(f"Your monthly payment = {payment}!")


def calculate_number_payments():
    global months
    months = math.ceil(math.log((payment / (payment - interest * principal)), (1 + interest)))
    mm = months % 12
    yy = months // 12
    string_months = "It will take "
    if yy > 0:
        string_months += (str(yy) + " year")
        if yy > 1:
            string_months += "s"
        string_months += " "
        if mm > 0:
            string_months += "and "
    if mm > 0:
        string_months += (str(mm) + " month")
        if mm > 1:
            string_months += "s"
        string_months += " "
    string_months += "to repay this loan!"
    print(string_months)


def are_numbers_ok():
    global principal, payment, months, interest
    if principal is not None:
        try:
            principal = float(principal)
        except ValueError:
            return False
        else:
            if principal < 0:
                return False
    if payment is not None:
        try:
            payment = float(payment)
        except ValueError:
            return False
        else:
            if payment < 0:
                return False
    if months is not None:
        try:
            months = int(months)
        except ValueError:
            return False
        else:
            if months < 0:
                return False
    if interest is not None:
        try:
            interest = float(interest) / 12 / 100
        except ValueError:
            return False
        else:
            if interest < 0:
                return False
    return True


def is_arguments_ok():
    if type_of_payment != "annuity" and type_of_payment != "diff":
        print("Incorrect parameters")
    elif type_of_payment == "diff" and (months is None or principal is None or payment is not None):
        print("Incorrect parameters")
    elif interest is None:
        print("Incorrect parameters")
    elif not are_numbers_ok():
        print("Incorrect parameters")
    else:
        return True
    return False


def calculate_differentiated_payment():
    global Dm_sum
    P = principal  # the loan principal
    i = interest  # nominal interest rate
    n = months  # number of payments
    Dm = list()
    Dm_sum = 0
    for m in range(n):
        Dm.append(math.ceil((P / n) + i * (P - ((P * (m)) / n))))
        print(f"Month {m + 1}: payment is {Dm[m]}")
        Dm_sum += Dm[m]


def calc_overpayment():
    global overpayment
    if Dm_sum is None:
        overpayment = (months * payment) - principal
    else:
        overpayment = Dm_sum - principal
    print(f"Overpayment = {overpayment}")


def what_will_calculate():
    if principal is None and payment is not None and months is not None:
        calculate_loan_principal()
    elif months is None and payment is not None and principal is not None:
        calculate_number_payments()
    elif payment is None and principal is not None and months is not None:
        if type_of_payment == "diff":
            calculate_differentiated_payment()
        else:
            calculate_monthly_payment()
    else:
        print("Incorrect parameters")


def command_line():
    global type_of_payment, payment, principal, months, interest

    parser = argparse.ArgumentParser(description="")

    # parser.add_argument("-t", "--type", choices=["annuity", "diff"], required=True)
    # parser.add_argument("-pay", "--payment", type=float)
    # parser.add_argument("-pri", "--principal", type=float)
    # parser.add_argument("-per", "--periods", type=int)
    # parser.add_argument("-i", "--interest", type=float, required=True)
    parser.add_argument("-t", "--type")
    parser.add_argument("-pay", "--payment")
    parser.add_argument("-pri", "--principal")
    parser.add_argument("-per", "--periods")
    parser.add_argument("-i", "--interest")

    args = parser.parse_args()

    type_of_payment = args.type
    payment = args.payment
    principal = args.principal
    months = args.periods
    interest = args.interest


def main():
    command_line()
    if is_arguments_ok():
        what_will_calculate()
        calc_overpayment()


main()
