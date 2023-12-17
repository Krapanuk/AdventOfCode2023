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
InvertedOnlyPipeArray = []
VSqueezePipeArray = []

#Definitions
#Read lines of file
file_path = currentdir+'/InputData/AOC101223input.txt'
#file_path = currentdir+'\InputData\AOC101223sample.txt'
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
	horizCoor = int(startCoor[0]) -1 # Add 1 or subtract 1
	verticCoor = int(startCoor[1]) # Add 1 or subtract 1
	actualCoor = [str(horizCoor), str(verticCoor)]
	moveCount = 0
	stop = False
	while stop == False:
		nextCoor = getNextCoorPosition(beforeCoor, actualCoor)
		if possibleMove(actualCoor, nextCoor) == True and inArea(nextCoor) == True and getElementType(nextCoor) != ".":
			beforeCoor = actualCoor
			actualCoor = nextCoor
			#writePipeToArray(actualCoor, "+")
			writePipeToArray(actualCoor, getElementType(actualCoor))
			moveCount += 1
		else: stop = True
	writeOnlyPipeArrayToFile(OnlyPipeArray, "output.txt")
	writeOnlyPipeArrayToFile(fillBlanksInOnlyPipeArray(OnlyPipeArray), "outputWithoutBlanks.txt")
	writeOnlyPipeArrayToFile(invertOnlyPipeArray(fillBlanksInOnlyPipeArray(OnlyPipeArray)), "outputInverted.txt")
	writeOnlyPipeArrayToFile(vSqueezesInPipeArray(OnlyPipeArray), "outputvSqueezed.txt")
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

def writeOnlyPipeArrayToFile(PArray, filename):
	with open(filename, "w") as txt_file:
		for line in PArray:
			txt_file.write("".join(line) + "\n")

def createOnlyPipeArray(PipeMap):
	for n in range(0, len(PipeMap)): 
		Line = []
		for m in range(0, len(PipeMap[n])):
			Line.append(" ")
		OnlyPipeArray.append(Line)
	return OnlyPipeArray

def fillBlanksInOnlyPipeArray(OnlyPipeArray):
	for n in range(0, len(OnlyPipeArray)): 
		for m in range(0, len(OnlyPipeArray[n])):	
			if n == 0 and m == 0: OnlyPipeArray[0][0] = "0"
			elif OnlyPipeArray[n-1][m] == "0" or OnlyPipeArray[n+1][m] == "0" or OnlyPipeArray[n][m-1] == "0" or OnlyPipeArray[n][m+1] == "0":
				if OnlyPipeArray[n][m] not in PipeTypePositions:
					OnlyPipeArray[n][m] = "0"
	for k in range(0, len(OnlyPipeArray)):
		i = len(OnlyPipeArray) - k -1
		for l in range(0, len(OnlyPipeArray[0])):
			j = len(OnlyPipeArray[0]) - l -1
			if i == len(OnlyPipeArray) and j == len(OnlyPipeArray[0]): print("Test")
			if OnlyPipeArray[i-1][j] == "0" or OnlyPipeArray[i+1][j] == "0" or OnlyPipeArray[i][j-1] == "0" or OnlyPipeArray[i][j+1] == "0":
				if OnlyPipeArray[i][j] not in PipeTypePositions:
					OnlyPipeArray[i][j] = "0"
	return OnlyPipeArray




def invertOnlyPipeArray(PArray):
	for n in range(0, len(PArray)): 
		Line = []
		for m in range(0, len(PArray[n])):
			if PArray[n][m] == " ": Line.append("+")
			elif PArray[n][m] in PipeTypePositions or PArray[n][m] == "0": Line.append(" ")
		InvertedOnlyPipeArray.append(Line)
	return InvertedOnlyPipeArray

def vSqueezesInPipeArray(PArray):
	for n in range(0, len(PArray)): 
		Line = []
		m = 0
		while m < len(PArray[n]):
			if PArray[n][m] == "7" and m < len(PArray[n]):
				if PArray[n][m+1] == "F":
					Line.append("||")
					m += 2
				else:
					Line.append(" ")
					m += 1
			elif PArray[n][m] == "|" and m < len(PArray[n]):
				if PArray[n][m+1] == "|":
					Line.append("||")
					m += 2
				else:
					Line.append(" ")
					m += 1
			elif PArray[n][m] == "J" and m < len(PArray[n]):
				if PArray[n][m+1] == "L":
					Line.append("||")
					m += 2
				else:
					Line.append(" ")
					m += 1
			elif PArray[n][m] == " ": 
				Line.append("+")
				m += 1
			elif PArray[n][m] in PipeTypePositions: 
				Line.append(" ")
				m += 1
			else: m += 1
		VSqueezePipeArray.append(Line)
	return VSqueezePipeArray

def writePipeToArray(coor, char):
	OnlyPipeArray[int(coor[0])][int(coor[1])] = char
	return OnlyPipeArray

print("S-Position = "+str(findS(readString(Lines))))
print(moveIteratively(findS(readString(Lines))))

#758 is too high
#701 is too high
#600 is too high
#400 is not right
#390 is not right