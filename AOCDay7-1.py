#Informations: My categories
#+5[6]:AAAAA: Five of a kind, where all five cards have the same label
#+4[5]Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#+3+1[4]:23332: Full house, where three cards have the same label, and the remaining two cards share a different label
#+2[3]:TTT98: Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand
#+1+1[2]:23432: Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label
#+1[1]:A23A4: One pair, where two cards share one label, and the other three cards have a different label from the pair and each other
#[0]:23456: High card, where all cards' labels are distinct

#Arrays
NumbersDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Data = [] #1st line
CardLabels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
Hands = []
resultArray = []
#The K has to be a higher number than the T
#The 5 has to be a higher number than the 4

#Definitions
def isLabelLetter(character):
	if character in CardLabelsLetters:
		return True
	else:
		return False
	
def isLabelDigit(character):
	if character in CardLabelsDigits:
		return True
	else:
		return False
	
def detectOfAKinds(hand):
	strongestValue = 0
	labelChar = ""
	for label in CardLabels: # For each label within CardLabels
		charCount = hand[0].count(label)
		if charCount > 1:
			strongestValue += 1
			if charCount > 2:
				strongestValue += 2
			if charCount == 4:
				strongestValue = 5
			if charCount == 5:
				#print("Test")
				strongestValue = 6
	hand.append(strongestValue)
	return hand

#Read lines of file
file_path = 'AOC071223input.txt'
#file_path = 'AOC071223sample.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

def readString(line):
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

def totalWinnings(Array):
	totalWin = 0
	elementCount = 1
	for i in range(0, len(Array)):
		for j in range(0, len(Array[i])):
			#print("Cal["+str(Array[i][j])+"]: Win = Bid "+str(Array[i][j][1])+" * Rank "+str(elementCount))
			totalWin = totalWin + (elementCount * int(Array[i][j][1]))
			elementCount += 1
	return totalWin

def sortArray(sub_li): # Sorts the given Array of one type by its char-values
	l = len(sub_li)
	#print("Test "+str(sub_li))
	for i in range(0, l):
		for j in range(0, l-i-1):
			#print(str(sub_li)+": "+str(sub_li[j][0])+" > "+str(sub_li[j+1][0])+" = "+str(cL1GrCl2(sub_li[j][0],sub_li[j+1][0])))
			#if (translateCardLabelToPos(sub_li[j][0]) < translateCardLabelToPos(sub_li[j+1][0])):
			if cL1GrCl2(sub_li[j][0],sub_li[j+1][0]) == 1:
				tempo = sub_li[j]
				sub_li[j] = sub_li[j + 1]
				sub_li[j + 1] = tempo
	return sub_li

def sortArrayNew2(sub_li): # Sorts the given Array of one type by its char-values
	l = len(sub_li)#print("Test "+str(sub_li))
	for n in range(0, 1000):
		for i in range(0, l):
			for j in range(0, l-1):     #print(str(sub_li)+": "+str(sub_li[j][0])+" > "+str(sub_li[j+1][0])+" = "+str(cL1GrCl2(sub_li[j][0],sub_li[j+1][0])))    #if (translateCardLabelToPos(sub_li[j][0]) < translateCardLabelToPos(sub_li[j+1][0])):
				if cL1GrCl2(sub_li[j][0],sub_li[j+1][0]) == 1: # if 1st > 2nd ...
					temp = sub_li[j]
					sub_li[j] = sub_li[j+1] # ... take the 2nd element at 1st elements position
					sub_li[j + 1] = temp
	return sub_li

def sortArrayNew(sub_li): # Sorts the given Array of one type by its char-values
	l = len(sub_li)
	sub_li.sort()
	print("Test "+str(sub_li))
	return sorted(sub_li, key=lambda li: li[0])

def cL1GrCl2(cL1, cL2):
	cL1GrCl2Marker = 0
	#print("Start cL1Gr..: cL1 " +cL1+" cL2 "+cL2)
	for c in range(0, len(cL1)):
		if cL1GrCl2Marker == 0:
			#if cL1 == "KTJJT": print("Compare "+str(cL1[c])+" ["+str(CardLabels.index(cL1[c]))+"] <"+str(cL2[c])+" ["+str(CardLabels.index(cL2[c]))+"]")
			if CardLabels.index(cL1[c]) < CardLabels.index(cL2[c]):
				#print(str(cL1[c])+" ["+str(CardLabels.index(cL1[c]))+"] > "+str(cL2[c])+" ["+str(CardLabels.index(cL2[c]))+"]")
				cL1GrCl2Marker = 1
			elif CardLabels.index(cL1[c]) > CardLabels.index(cL2[c]): 
				cL1GrCl2Marker = 2
				#print(str(cL1[c])+" ["+str(CardLabels.index(cL1[c]))+"] < "+str(cL2[c])+" ["+str(CardLabels.index(cL2[c]))+"]")
	#if cL1GrCl2Marker == 1: print("Test: "+str(cL1)+" > "+str(cL2))
	#elif cL1GrCl2Marker == 2: print("Test: "+str(cL1)+" < "+str(cL2))
	return cL1GrCl2Marker

lineCount = 0
counter = 0
for line in Lines:
	Hands.append(detectOfAKinds(readString(line)))

for type in range(0, 7):
	ArrayOfEachType = []
	for hand in Hands:
		if str(type) == str(hand[2]):
			ArrayOfEachType.append(hand)
	resultArray.append(sortArray(ArrayOfEachType))
print(str(resultArray))
print("Win: "+str(totalWinnings(resultArray)))
#151349862: too low
#250122737: No
#250274292: ?
#250337018: too low
#250410933: No
#250609767: too high
#250641781: ?
#250799231: ?

#Tests
#Test 1:
#if detectOfAKinds(readString("39933 111"))[2] != 4:
#	print("Test 1: Fehler")
#else: print("Test 1: Erfolg!")

if detectOfAKinds(readString("23456 111"))[2] != 0:
	print("Test 0: Fehler")
else: print("Test 0: Erfolg!")

if detectOfAKinds(readString("A23A4 111"))[2] != 1:
	print("Test 1: Fehler")
else: print("Test 1: Erfolg!")

if detectOfAKinds(readString("23432 111"))[2] != 2:
	print("Test 2: Fehler")
else: print("Test 2: Erfolg!")

if detectOfAKinds(readString("TTT98 111"))[2] != 3:
	print("Test 3: Fehler")
else: print("Test 3: Erfolg!")

if detectOfAKinds(readString("39933 111"))[2] != 4:
	print("Test 4: Fehler")
else: print("Test 4: Erfolg!")

if detectOfAKinds(readString("TTTT2 111"))[2] != 5:
	print("Test 5: Fehler")
else: print("Test 5: Erfolg!")

if detectOfAKinds(readString("AAAAA 111"))[2] != 6:
	print("Test 6: Fehler")
else: print("Test 6: Erfolg!")