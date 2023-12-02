#Arrays
NumbersString = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NumbersDigit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
sum = 0

#Definitions
def indexes(iterable, obj):
	return (index for index, elem in enumerate(iterable) if elem == obj)

def minimax(a):
	minpos = min(a)
	maxpos = max(a)
	return [minpos, maxpos]

def checkIfDigitBefore(c):
	lowestDigit = -1
	for numberDigit in NumbersDigit:
		if numberDigit in c:
			if lowestDigit < 0:
				lowestDigit = c.find(numberDigit)
			if c.find(numberDigit) < lowestDigit:
				lowestDigit = c.find(numberDigit)
	return lowestDigit

def checkIfDigitAfter(d):
	highestDigit = -1
	for numberDigit in NumbersDigit:
		if numberDigit in d:
			if highestDigit < 0:
				highestDigit = d.rfind(numberDigit)
			if d.rfind(numberDigit) > highestDigit:
				highestDigit = d.rfind(numberDigit)
	return highestDigit

def replaceFirstNumberString(b):
	numberStringCount = 0
	newStrLow = b
	newStrHigh = b
	lowestMatch = -1
	for numberString1 in NumbersString:
		if numberString1 in b:
			if lowestMatch < 0:
				lowestMatch = b.find(numberString1)
				newStrLow = b.replace(numberString1, NumbersDigit[numberStringCount], 1) # Just replace the lowest occurance
			if b.find(numberString1) < lowestMatch:
				lowestMatch = b.find(numberString1)
				newStrLow = b.replace(numberString1, NumbersDigit[numberStringCount], 1) # Just replace the lowest occurance
		numberStringCount += 1
	numberStringCount = 0
	if checkIfDigitBefore(b) > lowestMatch:
		new_str = newStrLow
	else:
		new_str = b
	highestMatch = -1
	for numberString2 in NumbersString:
		if numberString2 in new_str:
			if highestMatch < 0:
				highestMatch = b.rfind(numberString2) 
				newStrHigh = NumbersDigit[numberStringCount].join(new_str.rsplit(numberString2, 1)) # Just replace the highest occurance
			if b.rfind(numberString2) > highestMatch:
				highestMatch = b.rfind(numberString2)
				newStrHigh = NumbersDigit[numberStringCount].join(new_str.rsplit(numberString2, 1)) # Just replace the highest occurance
		numberStringCount += 1
	if checkIfDigitAfter(b) < highestMatch:
		new_str = newStrHigh
	else:
		new_str = newStrLow
	return new_str

#Read lines of file
file_path = 'AOC011223input.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()
lineCount = 0
for line in Lines:
	new_string = replaceFirstNumberString(line)
	numberCount = 0
	smallestNumberPos = []
	highestNumberPos = []
	highestLowestInListOfIndexes = []
	allNumbersInLine = []
	for number in NumbersDigit:
		idxs = indexes(new_string, number) #At what position(s) is the number within the new_string?
		listOfIndexes = list(idxs) #A List of all appearances of number within new_string - empty of there's none
		if len(listOfIndexes) == 1: #If the number is at at least one position within new_string (listOfIndexes ist not empty):
			if len(smallestNumberPos) == 0: #Initialize smallestNumberPos if empty
				smallestNumberPos = [listOfIndexes[0], number] 
			else:
				if listOfIndexes[0] < smallestNumberPos[0]:
					smallestNumberPos = [listOfIndexes[0], number]
			if len(highestNumberPos) == 0:
				highestNumberPos = [listOfIndexes[0], number]
			else:
				if listOfIndexes[0] > highestNumberPos[0]:
					highestNumberPos = [listOfIndexes[0], number]
		elif len(listOfIndexes) > 1: #If the number is at more than one position within new_string:
			highestLowestInListOfIndexes = minimax(listOfIndexes) #Array with the highest and lowest position of number
			if len(smallestNumberPos) == 0: #Initialize smallestNumberPos if empty
				smallestNumberPos = [highestLowestInListOfIndexes[0], number]
			else:
				if highestLowestInListOfIndexes[0] < smallestNumberPos[0]:
					smallestNumberPos = [highestLowestInListOfIndexes[0], number]
			if len(highestNumberPos) == 0:
				highestNumberPos = [highestLowestInListOfIndexes[1], number]
			else:
				if highestLowestInListOfIndexes[1] > highestNumberPos[0]:
					highestNumberPos = [highestLowestInListOfIndexes[1], number]
		allNumbersInLine.append(listOfIndexes)
	lineCount += 1
	twoDigitNumber = int(str(smallestNumberPos[1])+str(highestNumberPos[1]))
	sum = sum + twoDigitNumber 
	#print("Line "+str(lineCount)+": "+line+":"+str(twoDigitNumber))
print("Sum: "+str(sum))