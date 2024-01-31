import csv

def main():

    infile = open('employee_data.csv', 'r')

    csv_file = csv.reader(infile)

    next(csv_file)

    for rec in csv_file:
        salary = float(rec[3])
        bonus = float(rec[3]) * float(rec[7])
        pay = float(rec[3]) + bonus
        print(f'\nName: {rec[1]}\nSalary: $  {salary:8,.2f}\nBonus:  $  {bonus:8,.2f}\nPay:    $  {pay:8,.2f}')
        input()

main()