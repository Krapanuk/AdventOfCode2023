
#Arrays
NumbersDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SymbolPositions = []
NumberPositions = []
#This should look like:
#[
#[[234][Pos0:lineNumber,charPos]]
#[535][...]
#[84]
#]

#Definitions
def isSymbol(character):
	if character == '*':
		return True
	else:
		return False

#Definitions
def isDigit(character):
	if character in NumbersDigit:
		return True
	else:
		return False

def getNumberAndPos(lineSubstring, lineNumber, characterCount):
	numberAndPos = []
	charPos = 0
	foundNumberString = ""
	writingNumber = 1
	for character in lineSubstring:
		if isDigit(character) and writingNumber == 1: #If the character found is a numbers digit and we did not reach the last digit of the number
			foundNumberString = foundNumberString + character #Add the character(digit) to the found number
			if len(foundNumberString) > 1:
				numberAndPos[0] = foundNumberString #Don't add Number at position 0 if the first digit is already there: Just update number at pos 0
			else:
				numberAndPos.append(foundNumberString) #Add Number at position 0 to new numberAndPos-Array if it does not already exist
			numberAndPos.append([lineNumber, characterCount+charPos]) #Add each numbers position [lineNumber, charPos] to numberAndPos-Array
			charPos += 1
		else: #If the character found is NOT a numbers digit and we've just been writing a number reset: Finished writing the number increasing numberCount
			writingNumber = 0
	NumberPositions.append(addHitbox(numberAndPos))
	return charPos
		
def addHitbox(arrayOfNumbersAndPos):
	initialLineNr = arrayOfNumbersAndPos[1][0]
	if arrayOfNumbersAndPos[1][1] > 0: #Add a postion before the first digit, but only if the first digit is not already at position 0
		arrayOfNumbersAndPos.append([initialLineNr, arrayOfNumbersAndPos[1][1]-1])
		arrayOfNumbersAndPos.append([initialLineNr, arrayOfNumbersAndPos[len(arrayOfNumbersAndPos)-2][1]+1]) #Add a postion after the last digit (check position before last position (len-2) because I just addded position before first pos as last array value)
	else:
		arrayOfNumbersAndPos.append([initialLineNr, arrayOfNumbersAndPos[len(arrayOfNumbersAndPos)-1][1]+1]) #Add a postion after the last digit (check position before last position (len-2) because I just addded position before first pos as last array value)
	for i in range(1, len(arrayOfNumbersAndPos)):
		if initialLineNr > 0:
			arrayOfNumbersAndPos.append([initialLineNr-1, arrayOfNumbersAndPos[i][1]])
		arrayOfNumbersAndPos.append([initialLineNr+1, arrayOfNumbersAndPos[i][1]])
	return arrayOfNumbersAndPos

def sumIfIsPartNumber(NumberPos):
	sum = 0
	for x in range(0, len(NumberPos)): #For every number in NumberPositions ...
		found = 0
		for y in range(1, len(NumberPos[x])): #... and each of their Positions
			for s in range(0, len(SymbolPositions)):
				if NumberPos[x][y] == [SymbolPositions[s][1], SymbolPositions[s][2]] and found == 0:
					sum = sum + int(NumberPos[x][0])
					found = 1
	return sum

def multiplyIfInGearRange(NumberPos):
	sum = 0
	for x in range(0, len(NumberPos)): #For every number in NumberPositions ...
		found = 0
		for y in range(1, len(NumberPos[x])): #... and each of their Positions
			for s in range(0, len(SymbolPositions)):
				if NumberPos[x][y] == [SymbolPositions[s][1], SymbolPositions[s][2]] and found == 0:
					sum = sum + int(NumberPos[x][0])
					found = 1
	return sum



#Read lines of file
file_path = 'AOC031223input.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

#One Line per Game: Cut out Subgames
gameNumber = 1
lineCount = 0
skipCount = 0 #skip checking this number of values
for line in Lines:
	characterCount = 0
	for character in line:
		if skipCount > 0:
			skipCount -=1
		else:
			if isSymbol(character):
				SymbolPositions.append([character,lineCount, characterCount])
			elif isDigit(character):
				skipCount = getNumberAndPos(line[characterCount:], lineCount, characterCount)-1 #Call getNumberPos with substring from actual position to the end of the line
		characterCount += 1
	lineCount += 1
print(str(sumIfIsPartNumber(NumberPositions))) #525119