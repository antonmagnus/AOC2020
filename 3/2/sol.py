f  = open("3\\2\\input.txt")
treeLines = f.readlines()
iterations = [[1,1],[3,1],[5,1],[7,1],[1,2]]
mulTree = 1
for setting in iterations:
    numOfTrees = 0
    right, down = setting
    r = 0
    d = 0
    for index in range(0, len(treeLines), down):
        line = treeLines[index]
        if line[r%(len(line)-1)] == '#':
            numOfTrees +=1
        r+=right
    mulTree *=numOfTrees

print("number of trees: " + str(mulTree))
    