def main():

    infile = open('clients.txt','r')

    custnum = 0

    for line in infile:

        custnum += 1

        print(str(custnum) + '. ' + line.rstrip('\n'))


main()
