line = int(input("Enter the number of line:"))
def pattern6(line):
    space = line//2 +1
    star = 1
    for val in range(1,line+1):
        print(" "*space+"*"*star)
        star +=2
        space -=1
pattern6(line)
