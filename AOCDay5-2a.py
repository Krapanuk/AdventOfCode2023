#Arrays
NumbersDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Data = [] #1st line
SeedNumbers = []
SeedRange = []

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
file_path = 'AOC051223input.txt'
#file_path = '//wsl.localhost/Debian/home/beine/AdventOfCode2023/AOC051223sample.txt'
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
	foundInMap = 0
	minPos = 184859109092 	#Numbers = getNrRange(getNumbers(Lines[0])) 	#Numbers = ["79", "80"] #Sample: In my original Design the 1st value is the start of the seed-range and the 2nd is the end of seed range
	Numbers = ["50985980", "7961058"]
	#0Numbers = ["1848591090", "462385043"]
    #1Numbers = ["2611025720", "154883670"]
    #2Numbers = ["1508373603", "11536371"]
    #3Numbers = ["3692308424", "16905163"]
    #4Numbers = ["1203540561", "280364121"]
    #5Numbers = ["3755585679", "337861951"]
    #6Numbers = ["93589727",   "738327409"]
    #7Numbers = ["3421539474", "257441906"]
    #8Numbers = ["3119409201", "243224070"]
    #9Numbers = ["50985980",   "7961058"]

	#Numbers = ["3421539474", "257441906"]
	if int(Numbers[0]) == 55000000: print(str(Numbers))
	for s in range(int(Numbers[0]), int(Numbers[0])+int(Numbers[1])): # Check for all Seeds
		seed = int(s)
		actualDestination = int(s)
		for a in range(1, len(fullArray)): # Check for all Maps
			foundInMap = 0
			for p in range(1, len(fullArray[a])): # Check for all Maps' Valuesets
				destinationRange = int(fullArray[a][p][1]) + int(fullArray[a][p][2]) - 1
				if int(fullArray[a][p][1]) <= actualDestination <= destinationRange and foundInMap == 0: 
					foundInMap = 1
					actualDestination = actualDestination + int(fullArray[a][p][0]) - int(fullArray[a][p][1])	
					#print("Seed "+str(seed)+"'s actual Destination: "+str(actualDestination))
		if actualDestination < minPos:
			minPos = actualDestination
			#print(str(minPos))
	return(minPos)

def findPosOld(fullArray):
	foundInMap = 0
	minPos = 184859109092 	#Numbers = getNumbers(Lines[0]) 	#Numbers = getNrRange(getNumbers(Lines[0]))
	Numbers = ["79", "1"]
	print(str(Numbers))
	n = 2
	for c in range(0, len(Numbers)-1): # For all seed-ranges
		if c % n == 0:
			print(str(int(Numbers[c])))
			print(str(int(Numbers[c+1])))
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
                                    #print(str(actualDestination))
				if actualDestination < minPos:
					minPos = actualDestination
					#print(str(minPos))
	return(minPos)

def getNrRange(Numbers):
	n = 2
	for c in range(0, len(Numbers)-1):
			if c % n == 0: 
				if c == 0:
					SeedRange.append(int(Numbers[c]))
					SeedRange.append(int(Numbers[c]) + int(Numbers[c+1]))
					print("Initial: [0]:"+str(SeedRange[0])+", [1]"+str(SeedRange[1]))
				else:
					if SeedRange[0] > int(Numbers[c]):
						SeedRange[0] = int(Numbers[c])
					if SeedRange[1] < int(Numbers[c]) + int(Numbers[c+1]):
						SeedRange[1] = int(Numbers[c]) + int(Numbers[c+1])
					print("Then: [0]:"+str(SeedRange[0])+", [1]"+str(SeedRange[1]))
	return(SeedRange)

def getNrRangeCompareTest(Numbers):
	n = 2
	print("BEFORE: "+str(Numbers))
	for d in range(0, len(Numbers)-3):
		if d % n == 0: 
			for c in range(2, len(Numbers)-1):
				gap = 0
				if c % n == 0 and d != c: 
					#print("Combis: ["+str(d/2)+"]["+str(c/2)+"]")
					if int(Numbers[d]) < int(Numbers[c]) and int(Numbers[d+1]) > int(Numbers[c]) + int(Numbers[c+1]):
						print("C: [0]"+str(Numbers[c])+", [1]"+str(Numbers[c+1])+" completely in SeedRange [0]")
					if int(Numbers[d]) < int(Numbers[c]):
						print("Base: "+str(Numbers[d])+" < "+str(Numbers[c])+" partially in SeedRange [0]")
					if int(Numbers[d]) + int(Numbers[d+1]) > int(Numbers[c]) + int(Numbers[c+1]):
						print("Top: [0]"+str(int(Numbers[d]) + int(Numbers[d+1]))+" > "+str(int(Numbers[c]) + int(Numbers[c+1]))+" partially in SeedRange [0]")
	print("AFTER"+str(Numbers))
	return(Numbers)

lineCount = 0
blockCount = -1
for line in Lines:
	if line == "\n" or lineCount == 0: # Generate new Block for seeds, seed-to-soil..., ...
		blockCount += 1
		Data.append(readName(line))
	else: # If this is not a new block go line by line ...
		Data[blockCount].append(readName(line)) 
	lineCount += 1
print(str(findPos(Data))) #910845529
#print(str(getNrRange(getNumbers(Lines[0]))))
#3119409201
#95461669
#50985980 too low