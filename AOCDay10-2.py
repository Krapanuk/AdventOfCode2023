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
file_path = 'AOC101223input.txt'
#file_path = 'AOC101223sample.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

def inArea(coor):
	inArea = True
	if int(coor[0]) < 0 or int(coor[1]) < 0:
		inArea = False
	if int(coor[0]) > len(PipeMap) or int(coor[1]) > len(PipeMap[0]):
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
	#print(str(getMoveDirection(beforeCoor, actualCoor)))
	#print(str(PipeTypePositions.index(element)))
	#print(str(PipeTypes[pos]))
	if getMoveDirection(beforeCoor, actualCoor) in PipeTypes[pos]:
		possible = True
	return possible

def getNextMove(beforeCoor, actualCoor):
	element = getElementType(actualCoor)
	possible = False #3,0 => 3,1
	pos = PipeTypePositions.index(element)
	intermArray = PipeTypes[pos]
	#print(str(intermArray))
	#print(str(intermArray.index(getMoveDirection(beforeCoor, actualCoor))))
	#print(str(getMoveDirection(beforeCoor, actualCoor)))
	nextMoveDirection = ""
	if getMoveDirection(beforeCoor, actualCoor) in intermArray:
		if intermArray.index(getMoveDirection(beforeCoor, actualCoor)) == 0:
			nextMoveDirection = intermArray[1]
			#nextMoveDirection = intermArray.pop(intermArray.index(getMoveDirection(beforeCoor, actualCoor)))
		elif intermArray.index(getMoveDirection(beforeCoor, actualCoor)) == 1: 
			nextMoveDirection = intermArray[0]
	return nextMoveDirection

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

def moveIteratively(startCoor):
	beforeCoor = startCoor
	horizCoor = int(startCoor[0])  # Add 1 or subtract 1
	verticCoor = int(startCoor[1]) -1
	actualCoor = [str(horizCoor), str(verticCoor)]
	moveCount = 0
	stop = False
	while stop == False:
		nextCoor = getNextCoorPosition(beforeCoor, actualCoor)
		print("Test: nextCoor: "+ str(nextCoor))
		#print("Test: GetElementType: "+ getElementType(nextCoor))
		#print("Test: possibleMove: "+ str(possibleMove(actualCoor, nextCoor)) +" ["+str(actualCoor)+"]["+str(nextCoor)+"]")
		#print("Test: inArea: "+ str(inArea(nextCoor)))
		if possibleMove(actualCoor, nextCoor) == True and inArea(nextCoor) == True and getElementType(nextCoor) != ".":
			beforeCoor = actualCoor
			actualCoor = nextCoor
			moveCount += 1
		else: stop = True
	return str(moveCount)

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
#readString(Lines)
print(moveIteratively(findS(readString(Lines))))

#Result: (13225+1) / 2

#Tests:
#PositionChecks:
#3,0 => 4,0 (L)
if possibleMove(['3', '0'], ['4', '0']) == True:
	print("Testcase: possibleMove ['3', '0'], ['4', '0']: Success!")
else: print("Testcase: possibleMove: Error: ['3', '0'], ['4', '0'] (L)")
if possibleMove(['3', '0'], ['3', '1']) == False:
	print("Testcase: possibleMove ['3', '0'], ['3', '1']: Success!")
else: print("Testcase: possibleMove: Error: ['3', '0'], ['3', '1'] (F)")
if possibleMove(['4', '1'], ['4', '2']) == False:
	print("Testcase: possibleMove ['4', '1'], ['4', '2']: Success!")
else: print("Testcase: possibleMove: Error: ['4', '1'], ['4', '2'] (.))")
if possibleMove(['4', '0'], ['4', '1']) == True:
	print("Testcase: possibleMove ['4', '0'], ['4', '1']: Success!")
else: print("Testcase: possibleMove: Error: ['4', '0'], ['4', '1'] (J))")
if possibleMove(['3', '2'], ['3', '3']) == True:
	print("Testcase: possibleMove ['3', '2'], ['3', '3']: Success!")
else: print("Testcase: possibleMove: Error: ['3', '2'], ['3', '3'] (-))")

#getNextMove:
if getNextMove(['3', '0'], ['4', '0']) == "r":
	print("Testcase: getNextMove: Success!")
else: print("Testcase: getNextMove: Error: ['3', '0'], ['4', '0']: Is "+str(getNextMove(['3', '0'], ['4', '0']))+" and should be (r))")
if getNextMove(['4', '0'], ['4', '1']) == "u":
	print("Testcase: getNextMove: Success!")
else: print("Testcase: getNextMove: Error: ['4', '0'], ['4', '1']: Is "+str(getNextMove(['4', '0'], ['4', '1']))+" and should be (u))")

#getNextCoorPosition:
if getNextCoorPosition(['4', '0'], ['4', '1']) == ['3', '1']:
	print("Testcase: getNextCoorPosition: Success!")
else: print("Testcase: getNextCoorPosition: Error: ['4', '0'], ['4', '1']: Is "+str(getNextCoorPosition(['4', '0'], ['4', '1']))+" and should be ['3', '1']")