line =int(input('Enter the number of line:'))
def pattern10(line):
    for val in range(1,line+1):
        for ind in range(val):
            print('*',end=' ')
        print()
pattern10(line)
