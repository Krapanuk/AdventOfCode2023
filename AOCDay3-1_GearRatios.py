#My plan
#1) Find all symbol positions: Array of Pos with 2 values: Line number and String-Position [[LineNumber, StrinPos.], [], [], ...]
#2) Find all Number positions: Array of Number (pos 0) and the area/hitbox around them beginning with the line they'r in and they'r 1st character postion (pos 1)
#   a. Find all Numbers in each line
#       - Iterate trough the lines:
#       - when a Number digit is found (Array NumbersDigit) in a line
#       - get the rest of the number adding chars to the number string until the char is not in Numbers digit
#       - and add this number to NumberPositions Array NumberPositions.append(number)
#       - adding numbers 1st character position in the format [line, charPos] by NumberPositions.[].append([line, charPos])
#       - adding the positions of all other digits of the number by NumberPositions.[].append([line, charPos])
#   b. Create the number hitbox 

#Arrays
NumbersDigit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
	if character not in NumbersDigit and not ".":
		return 1
	else:
		return 0

#Definitions
def isDigit(character):
	if character in NumbersDigit:
		return 1
	else:
		return 0

def getNumberAndPos(lineSubstring, lineNumber, cPos):
	nextNumberPos = len(NumberPositions) + 1
	charPos = cPos
	foundNumberString = ""
	writingNumber = 1
	for character in lineSubstring:
		if isDigit and writingNumber: #If the character found is a numbers digit and we did not reach the last digit of the number
			foundNumberString = foundNumberString + character #Add the character(digit) to the found number
			if lenght(foundNumberString) > 1:
				NumberPositions[nextNumberPos][0] = foundNumberString #Don't add Number at position 0 if the first digit is already there: Just update number at pos 0
			else:
				NumberPositions[nextNumberPos].append(foundNumberString) #Add Number at position 0 to new numberAndPos-Array if it does not already exist
			NumberPositions[nextNumberPos].append([lineNumber, charPos]) #Add each numbers position [lineNumber, charPos] to numberAndPos-Array
		else: #If the character found is NOT a numbers digit and we've just been writing a number reset: Finished writing the number increasing numberCount
			writingNumber = 0
		charPos += 1
	return charPos
		
#def createHitbox

#def isPartNumber

#Read lines of file
file_path = 'AOC031223input.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

#One Line per Game: Cut out Subgames
gameNumber = 1
lineCount = 0
for line in Lines:
	characterCount = 0
	for character in line:
		if isSymbol:
			SymbolPositions.append(lineCount, characterCount)
		elif isDigit:
			characterCount = getNumberAndPos(line[characterCount:], lineCount, characterCount) #Call getNumberPos with substring from actual position to the end of the line
		characterCount += 1
	lineCount += 1
print("Sum: "+str(sumGameIDs))