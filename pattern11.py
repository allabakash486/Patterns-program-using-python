line =int(input('Enter the number of line:'))
def pattern11(line):
    for val in range(line,-1,-1):
        for ind in range(val):
            print('*',end=' ')
        print()
pattern11(line)