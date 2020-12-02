f  = open("1\input.txt")
pwList = f.readlines()

numOfValid = 0
numOfInValid = 0
for password in pwList:
    segments = password.split(' ')
    lowerLimit = segments[0].split('-')[0]
    upperLimit = segments[0].split('-')[1]
    letter = segments[1].strip(':')
    count = segments[2].strip('\n').count(letter)
    if count>=int(lowerLimit) and count<=int(upperLimit):
        numOfValid += 1
    else:
        numOfInValid +=1
print("invalid: " + str(numOfInValid))
print("valid: " + str(numOfValid))
    


