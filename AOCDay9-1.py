#Informations: 
# 1) Read all characters in the 1st 2 lines of the file in a string
# 2) Read all other lines >3 of the file in 
#    a. a Index-Array "Indices" with only the 1st
#    b. a string-Array with 3 Sub-Arrays per line
# 3) For all characters in the string:

#Arrays
InitIndices = [] # Only the (6) A-Positions
Indices = [] #Only the 1st of the 3 Array-Insights
Network = [] #Full Array

#Definitions
#Read lines of file
file_path = 'AOC081223input.txt'
#file_path = 'AOC081223sample3.txt'
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
					#print("["+str1+"]")
					Array.append(str1)
				foundString = ""
	Array.append(foundString)
	return Array

Instructions = ""
node = "AAA"
for l in range(0, 1):
	Instructions = Instructions + Lines[l].replace("\n", "")
for line in range(2, len(Lines)):
	InitIndices.append(readString(Lines[line])[0][2])
	Indices.append(readString(Lines[line])[0])
	Network.append(readString(Lines[line]))
Positions = []
for v in range (0, len(InitIndices)):
	if InitIndices[v] == "A":
		Positions.append(v)
#print("Initially: Positions of 3rd As: "+str(Positions))
steps = 0
instCount = 0
#print(str(Positions))
run = True
param = 0
while run:
	steps += 1	
	if Instructions[instCount] == "R": param = 2
	else: param = 1
	zCount = 0
	posCount = 0
	node = ""
	for pos in Positions: #In the Array at the give position "pos" (maybe convert to int) read the right[2] or left[1] value and get its position
		node = Network[pos][param]
		#print(node)
		if node[2] == "Z": 
			#print(node[2])
			zCount += 1
		Positions[posCount] = Indices.index(node)
		posCount += 1
	if instCount >= len(Instructions)-1: 
		instCount = 0
	else: instCount += 1
	if zCount == len(Positions): run = False
	#if steps > 10: run = False
	if zCount > 3: print("Positions = "+str(Positions)+" [zCount:"+str(zCount)+"]")
	if steps == 10000000: print("Steps > 10000000: "+str(steps)+" [Positions, "+str(Positions)+" zCount:"+str(zCount)+"]")
	if steps == 1000000000: print("Steps > 1000000000: "+str(steps)+" [Positions, "+str(Positions)+" zCount:"+str(zCount)+"]")
print("RESULT: "+str(steps))

#Result: 16897



#print("Index of node ["+node+"]: "+str(Indices.index(node)))
#print("Instruction:L "+str(Network[Indices.index(node)][param]))
#print("instCount="+str(instCount)+" and lenInstructions="+str(len(Instructions)))
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