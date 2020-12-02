pwList = open("2\input.txt").readlines()
numOfValid = 0
for password in pwList:
    segments = password.split(' ')
    posOne = segments[0].split('-')[0]
    posTwo = segments[0].split('-')[1]
    letter = segments[1].strip(':')
    text = segments[2].strip('\n')
    if (text[int(posOne)-1] is letter) ^ (text[int(posTwo)-1] is letter):
        numOfValid += 1
print("valid: " + str(numOfValid))
    


