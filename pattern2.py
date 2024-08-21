line = int(input("Enter the number of lines:"))
def pattern2(line):
    for val in range(1,line+1):
        print("*"*val,end=' ')
        print()
pattern2(line)