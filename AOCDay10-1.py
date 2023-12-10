#Informations: 
#| is a vertical pipe connecting north and south. => u,d
#- is a horizontal pipe connecting east and west. => l,r
#L is a 90-degree bend connecting north and east. => u,r
#J is a 90-degree bend connecting north and west. => u,l
#7 is a 90-degree bend connecting south and west. => d,l
#F is a 90-degree bend connecting south and east. => d,r

#Arrays
PipeMap = [] # All pipe positions
PipeTypePositions = ["|", "-", "L", "J", "7", "F", ".", "S", ] #All positions of types 'o pipes
PipeTypes = [["u", "d"], ["l", "r"], ["u", "r"], ["u", "l"], ["d", "l"], ["d", "r"], ["."], ["u", "d", "l", "r"], ] #All types 'o pipes

#Definitions
#Read lines of file
#file_path = 'AOC101223input.txt'
file_path = 'AOC101223sample.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

def readString(Lines):
	for line in Lines: 
		PipeMap.append(line)
	return PipeMap

def getElementType(coor):
	#print(str(PipeMap))
	return PipeMap[int(coor[0])][int(coor[1])]

def getMoveDirection(beforeCoor, actualCoor):
	direction = ""
	if beforeCoor[1] < actualCoor[1]: #Vertical moves: Like 2,2 => 2,3 (left to right)
		direction = "r" # ... so the Element must have one entrance at its left side
	else: direction = "l" #or 2,3 => 2,2 (right to left)
	if beforeCoor[0] > actualCoor[0]: #Horizontal moves: Like 2,4 => 3,4 (up to down)
		direction = "d" # ... so the Element must have one entrance at its upper side
	else: direction = "u" #or 3,4 => 2,4 (down to up)
	return direction

def possibleMove(beforeCoor, actualCoor):
	element = getElementType(actualCoor)
	possible = False #3,0 => 3,1
	pos = PipeTypePositions.index(element)
	if getMoveDirection(beforeCoor, actualCoor) in PipeTypes[pos]:
		possible = True
	return possible

def getNextMove(beforeCoor, actualCoor):
	element = getElementType(actualCoor)
	possible = False #3,0 => 3,1
	pos = PipeTypePositions.index(element)
	subArray = PipeTypes[pos]
	nextMoveDirection = ""
	if getMoveDirection(beforeCoor, actualCoor) in subArray:
		nextMoveDirection = subArray.pop(getMoveDirection(beforeCoor, actualCoor))
	return nextMoveDirection

def getNextPosition(beforeCoor, actualCoor):
	nextCoor = []
	#if possibleMove(beforeCoor, actualCoor) == True:
	#element = getElementType(actualCoor)

	return nextCoor

def findS(PipeMap):
	lineCount = 0
	sCoor = []
	sFound = False
	while sFound == False:
		if PipeMap[lineCount].find("S") != -1:
			sCoor.append(str(lineCount)) # Horizontal
			sCoor.append(str(PipeMap[lineCount].find("S"))) # Vertical
			sFound = True
		lineCount += 1
	return sCoor
#print("Line from PipeMap: "+str(readString(Lines)))
print("S-Position = "+str(findS(readString(Lines))))
readString(Lines)
#print("Get Element Type at Position 0, 1 = "+str(getElementType(['4', '0'])))
#print("RESULT: "+str(steps))
#Result: 

#Tests:
#PositionChecks:
#3,0 => 4,0 (L)
if possibleMove(['3', '0'], ['4', '0']) == True:
	print("Test: possibleMove: Success!")
else: print("Test: possibleMove: Error: ['3', '0'], ['4', '0'] (L)")
if possibleMove(['3', '0'], ['3', '1']) == False:
	print("Test: possibleMove: Success!")
else: print("Test: possibleMove: Error: ['3', '0'], ['3', '1'] (F)")
if possibleMove(['4', '1'], ['4', '2']) == False:
	print("Test: possibleMove: Success!")
else: print("Test: possibleMove: Error: ['4', '1'], ['4', '2'] (.))")