#Informations: 
#| is a vertical pipe connecting north and south. => u,d
#- is a horizontal pipe connecting east and west. => l,r
#L is a 90-degree bend connecting north and east. => u,r
#J is a 90-degree bend connecting north and west. => u,l
#7 is a 90-degree bend connecting south and west. => d,l
#F is a 90-degree bend connecting south and east. => d,r

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#Arrays
PipeMap = [] # All pipe positions
PipeTypePositions = ["|", "-", "L", "J", "7", "F", ".", "S", ] #All positions of types 'o pipes
PipeTypes = [["u", "d"], ["l", "r"], ["u", "r"], ["u", "l"], ["d", "l"], ["d", "r"], ["."], ["u", "d", "l", "r"], ] #All types 'o pipes
OnlyPipeArray = []

#Definitions
#Read lines of file
#file_path = '\InputData\AOC101223input.txt'
file_path = currentdir+'\InputData\AOC101223sample.txt'
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
		if intermArray.index(getMoveDirection(beforeCoor, actualCoor)) == 0:
			nextMoveDirection = intermArray[1]
		elif intermArray.index(getMoveDirection(beforeCoor, actualCoor)) == 1: 
			nextMoveDirection = intermArray[0]
	return nextMoveDirection

def getNextCoorPosition(beforeCoor, actualCoor):
	horizCoor = int(actualCoor[0])
	verticCoor = int(actualCoor[1])
	nextMovesDirection = getNextMove(beforeCoor, actualCoor)
	if nextMovesDirection == "u": horizCoor -= 1 #Moving up means reducing the horizCoor
	elif nextMovesDirection == "d": horizCoor += 1 #Moving down means increasing the horizCoor
	elif nextMovesDirection == "l": verticCoor -= 1
	elif nextMovesDirection == "r": verticCoor += 1
	nextCoor = [str(horizCoor), str(verticCoor)]
	return nextCoor

def moveIteratively(startCoor):
	createOnlyPipeArray(PipeMap)
	beforeCoor = startCoor
	writePipeToArray(startCoor, "S")
	horizCoor = int(startCoor[0]) +1 # Add 1 or subtract 1
	verticCoor = int(startCoor[1]) # Add 1 or subtract 1
	actualCoor = [str(horizCoor), str(verticCoor)]
	moveCount = 0
	stop = False
	while stop == False:
		nextCoor = getNextCoorPosition(beforeCoor, actualCoor)
		if possibleMove(actualCoor, nextCoor) == True and inArea(nextCoor) == True and getElementType(nextCoor) != ".":
			beforeCoor = actualCoor
			actualCoor = nextCoor
			writePipeToArray(actualCoor, "+")
			moveCount += 1
		else: stop = True
	writeOnlyPipeArrayToFile(OnlyPipeArray)
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

def writeOnlyPipeArrayToFile(PArray):
	with open("output.txt", "w") as txt_file:
		for line in PArray:
			txt_file.write(" ".join(line) + "\n")

def createOnlyPipeArray(PipeMap):
	for n in range(0, len(PipeMap)): 
		Line = []
		for m in range(0, len(PipeMap[n])):
			Line.append(" ")
		OnlyPipeArray.append(Line)
	return OnlyPipeArray

def writePipeToArray(coor, char):
	OnlyPipeArray[int(coor[0])][int(coor[1])] = char
	return OnlyPipeArray

print("S-Position = "+str(findS(readString(Lines))))
print(moveIteratively(findS(readString(Lines))))

#Result: (13225+1) / 2