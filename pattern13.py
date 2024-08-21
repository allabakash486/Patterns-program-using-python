line =int(input('Enter the number of line:'))
def pattern13(line):
    space ,star =0,line
    for val in range(1,line+1):
        for sp in range(space):
            print(' ',end=' ')
        for ind in range(star):
            print('*',end=' ')
        print()
        space +=1
        star -=1
pattern13(line)