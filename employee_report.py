import csv

def main():

    infile = open('employee_data.csv', 'r')

    csv_file = csv.reader(infile)

    next(csv_file)

    for rec in csv_file:

        productivity = rec[5]
        hours = rec[4]

        efficiency = productivity/hours

        if efficiency >= 2:
            

main()