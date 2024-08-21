line = int(input("Enter the number of lines:"))
def pattern3(line):
    for val in range(line,-1,-1):
        print("*"*val,end=' ')
        print()
pattern3(line)