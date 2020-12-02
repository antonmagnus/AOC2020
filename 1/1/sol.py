f  = open("1\input.txt")
lines = f.readlines()
lines.sort(key = int)
found = False
i = 0
j = len(lines)-1

while(not found):
    num1 = int(lines[i])
    num2 = int(lines[j])
    dif = 2020 - (num1+num2)
    if dif==0:
        print(num1*num2)
        found = True
    elif dif<0:
        j -=1
    elif dif>0:
        i +=1
    if(i==j):
        print("not found")
        break