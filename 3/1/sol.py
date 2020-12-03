f  = open("3\\1\\input.txt")
treeLines = f.readlines()

numOfTrees = 0
i=0
for line in treeLines:
    if line[i%(len(line)-1)] == '#':
        numOfTrees +=1
    i+=3
print("number of trees: " + str(numOfTrees))
    