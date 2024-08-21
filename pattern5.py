line = int(input("Enter the number of lines:"))
def pattern5(line):
    space =0 
    star = line-1
    for val in range(line):
        print(" "*space + "*"*star)   
        star -=1
        space +=1   
pattern5(line)