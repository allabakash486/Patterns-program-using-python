line = int(input("Enter the line:"))
def pattern9(line):
    space,star = 0,line
    for val in range(line//2+1):
        print(" "*space+"*"*star)
        space +=1
        star -=2
    space,star = 1,line//2+1
    for  val in range(line//2):
        print(" "*space+"*"*star)
        space -=1
        star +=2
pattern9(line)
