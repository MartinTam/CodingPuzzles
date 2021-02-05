typed = input('\nEnter the number of rows: ')
inputNumber = 0
printNumber = 1
row = 0
col = 0

try:
    inputNumber = int(typed)
except:
    inputNumber = 0

if inputNumber <= 0:
    print('Wrong number!')
else:
    print()
    while row != inputNumber:
        
        row += 1

        while col != row:

            print('{0} '.format(printNumber), end='')
            printNumber += 1
            col += 1
        
        print()
        col = 0
    print()