import csv

def main():

    infile = open('customers.csv', 'r')
    outfile = open('customer-country.csv', 'w')

    csv_file1 = csv.reader(infile)
    csv_file2 = csv.writer(outfile)

    next(csv_file1)

    for rec in csv_file1:
        outfile.write(f'{rec[1]} {rec[2]}, {rec[4]}\n')

    outfile.close


main()