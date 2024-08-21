line = int(input("Enter the lines:"))
def pattern7(line):
    space = line//2
    star = 1
    for val in range(line//2+1):
        print(" "*space+"*"*star)
        star += 2
        space -= 1
    space = 1
    star = line-2
    for val in range(line//2+1):
        print(" "*space+"*"*star)
        star -=2
        space +=1
pattern7(line)

