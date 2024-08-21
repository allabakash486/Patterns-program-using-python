line =int(input('Enter the number of line:'))
def pattern12(line):
    space ,star =line-1,1
    for val in range(1,line+1):
        for sp in range(space):
            print(' ',end=' ')
        for ind in range(star):
            print('*',end=' ')
        print()
        space -=1
        star +=1
pattern12(line)