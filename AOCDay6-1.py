#Arrays
NumbersDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Data = [] #1st line
SeedNumbers = []

#Definitions
def isDigit(character):
	if character in NumbersDigit:
		return True
	else:
		return False

def getNumbers(line):
	Numbers = []
	foundNumberString = ""
	writingNumber = 0
	for character in line: 		
		if isDigit(character): #If the character found is a numbers digit and we did not reach the last digit of the number
			writingNumber = 1
			foundNumberString = foundNumberString + character #Add the character(digit) to the found number
		if character == " ":
			writingNumber = 0
			if foundNumberString != "": Numbers.append(foundNumberString)
			foundNumberString = ""
	Numbers.append(foundNumberString)
	return Numbers

#Read lines of file
file_path = 'AOC061223input.txt'
#file_path = 'AOC061223sample.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

def readName(line):
	foundString = ""
	Array = []
	for character in line: 
		#if character != " " or != "\n": #If the character found is a numbers digit and we did not reach the last digit of the number
		if character != "\n":
			foundString = foundString + character #Add the character(digit) to the found number
			if character == " ":
				Array.append(foundString.replace(" ", ""))
				#print(str(Array))
				foundString = ""
	if foundString not in ["\n", "", " "]: Array.append(foundString)
	#print(str(Array))
	return Array

def findPos(fullArray):
	foundInMap = 0
	minPos = 184859109099
	Numbers = getNumbers(Lines[0])
	n = 2
	for c in range(0, len(Numbers)-1):
		if c % n == 0: 
			for a in range(0, int(Numbers[c+1])):
				seed = int(Numbers[c])+a
				actualDestination = int(Numbers[c])+a
				for a in range(1, len(fullArray)): # Check for all Maps
					foundInMap = 0
					for p in range(1, len(fullArray[a])): # Check for all Maps' Valuesets
						destinationRange = int(fullArray[a][p][1]) + int(fullArray[a][p][2]) - 1
						if int(fullArray[a][p][1]) <= actualDestination <= destinationRange and foundInMap == 0: 
							foundInMap = 1
							actualDestination = actualDestination + int(fullArray[a][p][0]) - int(fullArray[a][p][1])	
				if actualDestination < minPos:
					minPos = actualDestination
					print(str(minPos))
	return(minPos)

lineCount = 0
counter = 0
blockCount = -1
#for race in range(0, len(Lines)):
Times = getNumbers(Lines[0])
Distances = getNumbers(Lines[1])
ways2beatTheRecord = 1
for race in range(0, len(Times)):
	ways2win = 0
	velocity = 0
	for speed in range(0,int(Times[race])+1):
		travelTime = int(Times[race]) - speed
		distance = speed * travelTime
		if distance > int(Distances[race]):
			ways2win += 1
	ways2beatTheRecord = ways2beatTheRecord * ways2win
	ways2win =  0
print("Answer: "+str(ways2beatTheRecord))
#print(str(findPos(Data))) #910845529