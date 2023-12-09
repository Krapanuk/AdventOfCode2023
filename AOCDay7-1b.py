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
CardLabels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
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
	#print(str("Start detectOAC: ..."))
	strongestValue = 0
	labelChar = ""
	containsJ = 0
	manys = []
	for char in hand[0]: 
		if char == "J": 
			containsJ += 1
	for label in CardLabels: # For each label within CardLabels
		manys.append(hand[0].count(label))	
	#print(manys)
	manys.sort()
	#print(manys)
	if manys[len(manys)-1] == 5:
		strongestValue = 6
		#print("Five of a kind "+str(strongestValue))
	elif manys[len(manys)-1] == 4:
		strongestValue = 5
		if containsJ > 0: strongestValue +=1
		#print("Four of a kind "+str(strongestValue))
	elif manys[len(manys)-1] == 3:
		strongestValue = 3
		if containsJ > 0: strongestValue +=1
		if manys[len(manys)-2] == 2:
			strongestValue = 4
			if containsJ > 0: strongestValue +=1
			#strongestValue = 4 +containsJ CAUTION: Check if this is to change with the 2 lines before!!!
			#print("Full House "+str(strongestValue))
		#else: print("Three of a kind "+str(strongestValue))
	elif manys[len(manys)-1] == 2:
		strongestValue = 1
		if containsJ > 0: strongestValue +=1
		if manys[len(manys)-2] == 2:
			strongestValue = 2 +containsJ
			#print("Two Pair "+str(strongestValue)) 
		#else: print("One Pair "+str(strongestValue))
	if containsJ > 0:
		strongestValue = strongestValue+1
	#print("ContainsJ "+str(containsJ))
	#print("ContainsJ add "+str(strongestValue))
	if strongestValue > 6:
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
#249010697: Wrong
#249010697

#Tests
#Test 1:
#if detectOfAKinds(readString("39933 111"))[2] != 4:
#	print("Test 1: Fehler")
#else: print("Test 1: Erfolg!")

if detectOfAKinds(readString("23K56 111"))[2] != 0:
	print("Test 0 [23456]: Error: Found["+str(detectOfAKinds(readString("23456 111"))[2])+"], Expected[0]")
else: print("Test 0: Erfolg!")
if detectOfAKinds(readString("AK3A4 111"))[2] != 1:
	print("Test 1 [A23A4]: Error: Found["+str(detectOfAKinds(readString("A23A4 111"))[2])+"], Expected[1]")
else: print("Test 1: Erfolg!")
if detectOfAKinds(readString("23432 111"))[2] != 2:
	print("Test 2 [23432]: Error: Found["+str(detectOfAKinds(readString("23432 111"))[2])+"], Expected[2]")
else: print("Test 2: Erfolg!")
if detectOfAKinds(readString("TTT98 111"))[2] != 3:
	print("Test 3 [TTT98]: Error: Found["+str(detectOfAKinds(readString("TTT98 111"))[2])+"], Expected[3]")
else: print("Test 3: Erfolg!")
if detectOfAKinds(readString("39933 111"))[2] != 4:
	print("Test 4 [39933]: Error: Found["+str(detectOfAKinds(readString("39933 111"))[2])+"], Expected[4]")
else: print("Test 4: Erfolg!")
if detectOfAKinds(readString("TTTT2 111"))[2] != 5:
	print("Test 5 [TTTT2]: Error: Found["+str(detectOfAKinds(readString("TTTT2 111"))[2])+"], Expected[5]")
else: print("Test 5: Erfolg!")
if detectOfAKinds(readString("AAAAA 111"))[2] != 6:
	print("Test 6 [AAAAA]: Error: Found["+str(detectOfAKinds(readString("AAAAA 111"))[2])+"], Expected[6]")
else: print("Test 6: Erfolg!")

if detectOfAKinds(readString("23456 111"))[2] != 0:
	print("Test 0 [23456]: Error: Found["+str(detectOfAKinds(readString("23456 111"))[2])+"], Expected[0]")
else: print("Test 0: Erfolg!")
if detectOfAKinds(readString("J23A4 111"))[2] != 1:
	print("Test J1 [J23A4]: Error: Found["+str(detectOfAKinds(readString("J23A4 111"))[2])+"], Expected[1]")
else: print("Test J1: Erfolg!")
if detectOfAKinds(readString("J3432 111"))[2] != 3:
	print("Test J2 [J3432]: Error: Found["+str(detectOfAKinds(readString("J3432 111"))[2])+"], Expected[3]")
else: print("Test J2: Erfolg!")
if detectOfAKinds(readString("TTJ98 111"))[2] != 3:
	print("Test J3 [TTJ98]: Error: Found["+str(detectOfAKinds(readString("TTJ98 111"))[2])+"], Expected[3]")
else: print("Test J3 [TTJ98]: Erfolg!")
if detectOfAKinds(readString("399J3 111"))[2] != 4:
	print("Test J4 [399J3]: FullHouse: Error: Found["+str(detectOfAKinds(readString("399J3 111"))[2])+"], Expected[4]")
else: print("Test J4: Erfolg!")
if detectOfAKinds(readString("T55J5 111"))[2] != 5:
	print("Test J5-1 [T55J5]: Error: Found["+str(detectOfAKinds(readString("T55J5 111"))[2])+"], Expected[5]")
else: print("Test J5-1 [T55J5]: Erfolg!")
if detectOfAKinds(readString("KTJJT 111"))[2] != 5:
	print("Test J5-2 [KTJJT]: Error: Found["+str(detectOfAKinds(readString("KTJJT 111"))[2])+"], Expected[5]")
else: print("Test J5-2 [KTJJT]: Erfolg!")
if detectOfAKinds(readString("QQQJA 111"))[2] != 5:
	print("Test J5-3 [QQQJA]: Error: Found["+str(detectOfAKinds(readString("QQQJA 111"))[2])+"], Expected[5]")
else: print("Test J5-3 [QQQJA]: Erfolg!")
if detectOfAKinds(readString("KJJJT 111"))[2] != 5:
	print("Test J5-4 [KJJJT]: Error: Found["+str(detectOfAKinds(readString("KJJJT 111"))[2])+"], Expected[5]")
else: print("Test J5-4 [KJJJT]: Erfolg!")
if detectOfAKinds(readString("KJJJJ 111"))[2] != 6:
	print("Test J6-1 [KJJJJ]: Error: Found["+str(detectOfAKinds(readString("KJJJJ 111"))[2])+"], Expected[6]")
else: print("Test J6-1 [KJJJJ]: Erfolg!")
if detectOfAKinds(readString("AAAAJ 111"))[2] != 6:
	print("Test J6 [AAAAJ]: Error: Found["+str(detectOfAKinds(readString("AAAAJ 111"))[2])+"], Expected[6]")
else: print("Test J6 [AAAAJ]: Erfolg!")