line = int(input("Enter the number of lines:"))
def pattern4(line):
    space = line-1
    star = 1
    for val in range(line):
        print(" "*space + "*"*star)   
        space -=1
        star +=1   
pattern4(line)