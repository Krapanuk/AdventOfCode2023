
#Arrays
NumbersString = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NumbersDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sum = 0

#Definitions
def indexes(iterable, obj):
	return (index for index, elem in enumerate(iterable) if elem == obj)

def minimax(a):
	minpos = min(a)
	maxpos = max(a)
	return [minpos, maxpos]

#Read lines of file
file_path = 'AOC011223input.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()
lineCount = 0
for line in Lines:
	lineCount += 1 #print("Line{}: {}".format(count, line.strip()))
	numberStringCount = 0
	print("Original String: "+line)
	new_string = line
	#for numberString in NumbersString:
	#	new_string = new_string.replace(numberString, NumbersDigit[numberStringCount])
	#	numberStringCount += 1
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
	print("Numbers in line "+new_string+" at position(s) "+str(allNumbersInLine))
	print("Lowest Number: " +str(smallestNumberPos[1])+" at Position "+ str(smallestNumberPos[0]))
	print("Highest Number: " +str(highestNumberPos[1])+" at Position "+ str(highestNumberPos[0]))
	print("Two Digit Number: "+ str(twoDigitNumber) + "[Actual Sum: "+str(sum)+"]")