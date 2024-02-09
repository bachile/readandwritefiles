import csv

def main():

    infile = open('employee_data.csv', 'r')

    csv_file = csv.reader(infile)

    next(csv_file)

    efficient = []
    inefficient = []  

    fourties = []
    thirties = []
    twenties = []

    for rec in csv_file:

        name = rec[1]
        age = int(rec[2])
        productivity = int(rec[5])
        hours = int(rec[4])

        efficiency = productivity/hours

        if efficiency > 2:
            efficient.append(name)
        if efficiency < 1:
            inefficient.append(name)

        if age >= 40:
            fourties.append(name)
        elif age >= 30:
            thirties.append(name)
        else:
            twenties.append(name)

    print('\nHighly Efficient Individuals:')
    for person in efficient:
        print(person)

    print('\n\nLow Efficiency Individuals:')
    for person in inefficient:
        print(person)

    print('\n\nEmployees in their 40s:')
    for person in fourties:
        print(person)
    print('\nTotal number of emplyees in their 40s:', len(fourties))

    print('\n\nEmployees in their 30s:')
    for person in thirties:
        print(person)
    print('\nTotal number of emplyees in their 30s:', len(thirties))

    print('\n\nEmployees in their 20s:')
    for person in twenties:
        print(person)
    print('\nTotal number of emplyees in their 20s:', len(twenties))
        
    print()

main()
