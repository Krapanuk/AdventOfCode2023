#Procedure
# 1) Read each line as an array of all numbers within an array of all lines
# 2) To the array for each line append another array with alle differences 
#    a. for all lines within the array: for l in range (0, len(ArrayOfAllLines)):
#       for all difference-Valuesets: for dS in range (0, len(ArrayOfAllLines[l])):
#       create temporary array for the diffs: DiffArray = []
#       for all values within the first to the last sub-Array: for i in range (1, len(ArrayOfAllLines[l][dS])):
#       calculate des difference: 
#          1stValue = int(ArrayOfAllLines[l][dS][i-1])
#          2ndValue = int(ArrayOfAllLines[l][dS][i])
#          if 1stValue > 2ndValue: difference = 1stValue - 2ndValue
#          else: difference = 2ndValue - 1stValue
#       append those differences: DiffArray.append(difference)
#    b. ArrayOfAllLines[LineNr].append[DiffArray]

#Arrays
ArrayOfAllLines = [] #Full Array

#Definitions
#Read lines of file
file_path = 'AOC091223input.txt'
#file_path = 'AOC091223sample.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

def readString(line):
	foundString = ""
	Array = []
	for character in line: 
		if character != "\n" and character != "=" and character != "(" and character != ")" and character != ",":
			foundString = foundString + character #Add the character(digit) to the found number
			if character == " ":
				str1 = foundString.replace(" ", "")
				if str1 != "":
					Array.append(str1)
				foundString = ""
	Array.append(foundString)
	return Array

def result(startSum):
	overallSum = startSum
	for n in range(0, len(ArrayOfAllLines)): # For each Sub-Array in ArrayOfAllLines
		lineSum = 0
		lenSubMain = len(ArrayOfAllLines[n])-1 # Get the number of Sub-IterationArrays within each SubArray of ArrayOfAllLines
		previousLinesFirstValue = 0
		linesFirstValue = 0
		length = len(ArrayOfAllLines[n][lenSubMain])-1
		for m in range(0, lenSubMain+1): # For each of those Sub-IterationArrays, from the last to the 1st (lenSubMain-m) take its last element		
			linesFirstValue = int(ArrayOfAllLines[n][lenSubMain-m][0]) 
			if m > 0: 
				previousLinesFirstValue = int(ArrayOfAllLines[n][lenSubMain-m+1][0]) - previousLinesFirstValue
			lineSum = linesFirstValue - previousLinesFirstValue
			ArrayOfAllLines[n][lenSubMain-m].append(str(linesFirstValue - previousLinesFirstValue))
		overallSum = overallSum + lineSum
	return overallSum

def addMissings(SubArray):
	checkCount = 0
	everythingsZero = False
	DiffIterations = []
	DiffIterations.append(SubArray)
	while everythingsZero == False:
		DiffArray = []
		everythingsZero = True
		for i in range (1, len(DiffIterations[checkCount])): # For all values in (Sub)SubArray at position checkCount of the Array SubArray
			firstValue = int(DiffIterations[checkCount][i-1])
			secondValue = int(DiffIterations[checkCount][i])
			difference = secondValue - firstValue
			DiffArray.append(str(difference))
			if difference != 0: everythingsZero = False
		DiffIterations.append(DiffArray)
		checkCount += 1
	return(DiffIterations)

def ideas():
	for l in range (0, len(ArrayOfAllLines)):
		for dS in range (0, len(ArrayOfAllLines[l])):
			DiffArray = []
			for i in range (1, len(ArrayOfAllLines[l][dS])):
				firstValue = int(ArrayOfAllLines[l][dS][i-1])
				secondValue = int(ArrayOfAllLines[l][dS][i])
				if firstValue > secondValue: difference = firstValue - secondValue
				else: difference = secondValue - firstValue
				DiffArray.append(difference)
			ArrayOfAllLines[l].append[DiffArray]

for line in Lines: # Create ArrayOfAllLines
	ArrayOfAllLines.append(addMissings(readString(line)))
print(str(result(0)))

#Results: 988