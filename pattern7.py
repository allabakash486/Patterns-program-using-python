line = int(input("Enter the number of lines:"))
def pattern7(line):
    space,star= 0,2*line-1
    for val in range(1,line+1):
        print(" "*space+"*"*star)
        star -=2
        space +=1
pattern7(line)
