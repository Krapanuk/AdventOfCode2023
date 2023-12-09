#Informations: 
# 1) Read all characters in the 1st 2 lines of the file in a string
# 2) Read all other lines >3 of the file in a string-Array with 3 Sub-Arrays per line
# 3) For all characters in the string:

#Arrays
#NumbersDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Indices = []
Network = []
#Data = []
#CardLabels = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
#Hands = []
#resultArray = []
#The K has to be a higher number than the T
#The 5 has to be a higher number than the 4

#Definitions

#Read lines of file
file_path = 'AOC081223input.txt'
#file_path = 'AOC081223sample2.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

def readString(line):
	foundString = ""
	Array = []
	for character in line: 
		if character != "\n" and character != "=" and character != "(" and character != ")" and character != ",":
			foundString = foundString + character #Add the character(digit) to the found number
			if character == " ":
				Array.append(foundString.replace(" ", ""))
				foundString = "" #if foundString not in ["\n", "", " "]: Array.append(foundString)
	Array.append(foundString)
	return Array


Instructions = ""
node = "AAA"
for l in range(0, 1):
	Instructions = Instructions + Lines[l].replace("\n", "")
for line in range(2, len(Lines)):
	Indices.append(readString(Lines[line])[0])
	Network.append(readString(Lines[line]))
steps = 0
instCount = 0
print("["+Instructions+"]")
while node != "ZZZ":
	steps += 1
	print("instCount="+str(instCount)+" and lenInstructions="+str(len(Instructions)))
	if Instructions[instCount] == "R":
		#print("Index of node ["+node+"]: "+str(Indices.index(node)))
		#print("Instruction:R "+str(Network[Indices.index(node)][3]))
		node = Network[Indices.index(node)][3]
	else: 
		#print("Index of node ["+node+"]: "+str(Indices.index(node)))
		#print("Instruction:L "+str(Network[Indices.index(node)][2]))
		node = Network[Indices.index(node)][2]
	if instCount >= len(Instructions)-1: 
		instCount = 0
	else: instCount += 1
print("RESULT: "+str(steps))

#Result: 16897