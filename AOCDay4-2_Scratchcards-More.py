#Arrays
NumbersDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
WinningNumbers = [] #1st part of the line
ElfsNumbers = [] #2nd part of the line
MatchingNumbers = []

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

def getNumbers(lineSubstring, lineNumber, isWinningNr):
	foundNumberString = ""
	writingNumber = 1
	for character in lineSubstring: 
		if isDigit(character) and writingNumber == 1: #If the character found is a numbers digit and we did not reach the last digit of the number
			foundNumberString = foundNumberString + character #Add the character(digit) to the found number
		else: #If the character found is NOT a numbers digit and we've just been writing a number reset: Finished writing the number increasing numberCount
			writingNumber = 0
	if isWinningNr == 1:
		WinningNumbers[lineNumber].append(foundNumberString)
	else:
		ElfsNumbers[lineNumber].append(foundNumberString)
	return len(foundNumberString)

def countHitsPerLine(lineNumber): #Compare, for each line, the elfs numbers to the winning numbers ...
	countWinningNrs = 0
	cardValue = 0
	numCount = 0
	for num in ElfsNumbers[lineNumber]:
		if ElfsNumbers[lineNumber][numCount] in WinningNumbers[lineNumber]:
			countWinningNrs += 1
		numCount += 1
	MatchingNumbers.append([lineNumber, countWinningNrs, 1])
	return countWinningNrs

def escalates(MatchingNumbers):
	countMatchingNrs = 0
	for matchingNumber in MatchingNumbers: #For each line and number of macthes in MatchingNumbers
		if MatchingNumbers[countMatchingNrs][1] > 0: # if there are more than 0 matches
			for m in range(0, int(MatchingNumbers[countMatchingNrs][2])): #for the number of cards
				for n in range(1, int(MatchingNumbers[countMatchingNrs][1])+1): #for the number of machtes
					MatchingNumbers[countMatchingNrs+n][2] = int(MatchingNumbers[countMatchingNrs+n][2]) + 1 #add 1 Card
		countMatchingNrs += 1
	sum = 0
	for match in MatchingNumbers: 
		sum = sum + int(match[2])
	print(MatchingNumbers)
	return sum

#Read lines of file
file_path = 'AOC041223input.txt'
#file_path = 'AOC041223sample.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

lineCount = 0
skipCount = 0 #skip checking this number of values
sum = 0
for line in Lines:
	winningNumbers = 1
	WinningNumbers.append([])
	ElfsNumbers.append([])
	characterCount = 10
	for character in line[10:]:
		if skipCount > 0:
			skipCount -=1
		else:
			if isDigit(character):
				skipCount = getNumbers(line[characterCount:], lineCount, winningNumbers)
			elif isSeparator(character):
				winningNumbers = 0
		characterCount += 1
	sum = sum + countHitsPerLine(lineCount)
	lineCount += 1
print(escalates(MatchingNumbers))