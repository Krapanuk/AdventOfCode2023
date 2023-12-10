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

def inArea(coor):
	inArea = True
	if coor[0] < 0 or coor[1] < 0:
		inArea = False
	if coor[0] > len(PipeMap) or coor[1] > len(PipeMap[0]):
		inArea = False
	return inArea

def readString(Lines):
	for line in Lines: 
		PipeMap.append(line)
	return PipeMap

def getElementType(coor):
	#print(str(PipeMap))
	return PipeMap[int(coor[0])][int(coor[1])]

def getMoveDirection(beforeCoor, actualCoor): #4,0 => 4,1: r
	direction = ""
	#print("beforeCoor:"+str(beforeCoor)+", actualCoor:"+str(actualCoor))
	if int(beforeCoor[1]) < int(actualCoor[1]): #Vertical moves: Like 2,2 => 2,3 (left to right)
		direction = "l" # ... so the Element must have one entrance at its left side
	elif int(beforeCoor[1]) > int(actualCoor[1]): 
		direction = "r" #or 2,3 => 2,2 (right to left)
	if int(beforeCoor[0]) > int(actualCoor[0]): #Horizontal moves: Like 2,4 => 3,4 (up to down)
		direction = "d" # ... so the Element must have one entrance at its upper side
	elif int(beforeCoor[0]) < int(actualCoor[0]):
		direction = "u" #or 3,4 => 2,4 (down to up)
	return direction

def possibleMove(beforeCoor, actualCoor):
	element = getElementType(actualCoor)
	possible = False 
	pos = PipeTypePositions.index(element)
	if getMoveDirection(beforeCoor, actualCoor) in PipeTypes[pos]:
		possible = True
	return possible

def getNextMove(beforeCoor, actualCoor):
	element = getElementType(actualCoor)
	possible = False #3,0 => 3,1
	pos = PipeTypePositions.index(element)
	intermArray = PipeTypes[pos]
	nextMoveDirection = ""
	if getMoveDirection(beforeCoor, actualCoor) in intermArray:
		nextMoveDirection = intermArray.pop(intermArray.index(getMoveDirection(beforeCoor, actualCoor)))
	return intermArray[0]

def getNextCoorPosition(beforeCoor, actualCoor):
	horizCoor = int(actualCoor[0])
	verticCoor = int(actualCoor[1])
	nextMovesDirection = getNextMove(beforeCoor, actualCoor)
	#print("Coor: beforeCoor" + str(beforeCoor) +"actualCoor" + str(actualCoor))
	if nextMovesDirection == "u": horizCoor -= 1 #Moving up means reducing the horizCoor
	elif nextMovesDirection == "d": horizCoor += 1 #Moving down means increasing the horizCoor
	elif nextMovesDirection == "l": verticCoor -= 1
	elif nextMovesDirection == "r": verticCoor += 1
	nextCoor = [str(horizCoor), str(verticCoor)]
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
print("S-Position = "+str(findS(readString(Lines))))
readString(Lines)


#print("RESULT: "+str(steps))
#Result: 

#Tests:
#PositionChecks:
#3,0 => 4,0 (L)
if possibleMove(['3', '0'], ['4', '0']) == True:
	print("Test: possibleMove ['3', '0'], ['4', '0']: Success!")
else: print("Test: possibleMove: Error: ['3', '0'], ['4', '0'] (L)")
if possibleMove(['3', '0'], ['3', '1']) == False:
	print("Test: possibleMove ['3', '0'], ['3', '1']: Success!")
else: print("Test: possibleMove: Error: ['3', '0'], ['3', '1'] (F)")
if possibleMove(['4', '1'], ['4', '2']) == False:
	print("Test: possibleMove ['4', '1'], ['4', '2']: Success!")
else: print("Test: possibleMove: Error: ['4', '1'], ['4', '2'] (.))")
if possibleMove(['4', '0'], ['4', '1']) == True:
	print("Test: possibleMove ['4', '0'], ['4', '1']: Success!")
else: print("Test: possibleMove: Error: ['4', '0'], ['4', '1'] (J))")

#getNextMove:
if getNextMove(['3', '0'], ['4', '0']) == "r":
	print("Test: getNextMove: Success!")
else: print("Test: getNextMove: Error: ['3', '0'], ['4', '0']: Is "+str(getNextMove(['3', '0'], ['4', '0']))+" and should be (r))")
if getNextMove(['4', '0'], ['4', '1']) == "u":
	print("Test: getNextMove: Success!")
else: print("Test: getNextMove: Error: ['4', '0'], ['4', '1']: Is "+str(getNextMove(['4', '0'], ['4', '1']))+" and should be (u))")

#getNextCoorPosition:
if getNextCoorPosition(['4', '0'], ['4', '1']) == ['3', '1']:
	print("Test: getNextCoorPosition: Success!")
else: print("Test: getNextCoorPosition: Error: ['4', '0'], ['4', '1']: Is "+str(getNextCoorPosition(['4', '0'], ['4', '1']))+" and should be ['3', '1']")