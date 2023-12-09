#Arrays
NumbersDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Data = [] #1st line
finalSeedPos = []

#Definitions
def isSeparator(character):
	if character == "|":
		return True
	else:
		return False

def isDigit(character):
	if character in NumbersDigit:
		return True
	else:
		return False

def getNumbers(lineSubstring, lineNumber):
	foundNumberString = ""
	writingNumber = 1
	for character in lineSubstring: 
		if isDigit(character) and writingNumber == 1: #If the character found is a numbers digit and we did not reach the last digit of the number
			foundNumberString = foundNumberString + character #Add the character(digit) to the found number
		else: #If the character found is NOT a numbers digit and we've just been writing a number reset: Finished writing the number increasing numberCount
			writingNumber = 0
	return len(foundNumberString)

#Read lines of file
#file_path = 'AOC051223input.txt'
file_path = '//wsl.localhost/Debian/home/beine/AdventOfCode2023/AOC051223sample.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

def readName(line):
	foundString = ""
	Array = []
	for character in line: 
		if character != "\n":
			foundString = foundString + character #Add the character(digit) to the found number
			if character == " ":
				Array.append(foundString.replace(" ", ""))
				foundString = ""
	if foundString not in ["\n", "", " "]: Array.append(foundString)
	return Array

def findPos(fullArray):
	finalSeedPos = []
	foundInMap = 0
	for s in range(1, len(fullArray[0])): # Check for all Seeds
		seed = int(fullArray[0][s])
		actualDestination = int(fullArray[0][s])
		for a in range(1, len(fullArray)): # Check for all Maps
			foundInMap = 0
			for p in range(1, len(fullArray[a])): # Check for all Maps' Valuesets
				destinationRange = int(fullArray[a][p][1]) + int(fullArray[a][p][2]) - 1
				if int(fullArray[a][p][1]) <= actualDestination <= destinationRange and foundInMap == 0: 
					foundInMap = 1
					actualDestination = actualDestination + int(fullArray[a][p][0]) - int(fullArray[a][p][1])
		finalSeedPos.append(actualDestination)	
	return(finalSeedPos)

lineCount = 0
counter = 0
blockCount = -1
for line in Lines:
	counter +=1
	if line == "\n" or lineCount == 0: # Generate new Block for seeds, seed-to-soil..., ...
		blockCount += 1
		Data.append(readName(line))
	else: # If this is not a new block go line by line ...
		Data[blockCount].append(readName(line)) 
	lineCount += 1
print(str(findPos(Data))) #910845529