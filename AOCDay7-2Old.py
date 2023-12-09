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
	
def detectOfAKindsOLD(hand):
	strongestValue = 0
	labelChar = ""
	for label in CardLabels: # For each label within CardLabels
		labelCount = -1
		for letter in hand[0]: # compare to each letter in line-Array's 1st position
			if letter == label: # If this letter exists in line-Array's 1st position add 1
				if labelCount == 0: labelCount += 1
				elif labelCount == 1: labelCount += 2
				elif labelCount == 2: labelCount += 3
				if labelCount > 0: labelChar = letter
		if labelCount > strongestValue:
			strongestValue = labelCount
	strongestValue2 = 0
	for label2 in CardLabels: # For each label within CardLabels
		#print(labelChar)
		if label2 != labelChar:
			labelCount2 = -1
			for letter2 in hand[0]: # compare to each letter in line-Array's 1st position
				if letter2 == label2: # If this letter exists in line-Array's 1st position add 1
					labelCount2 += 1
					if labelCount2 > 0: 
						#print("2test")
						strongestValue2 += 1
		if labelCount > strongestValue2:
			strongestValue2 = labelCount
	if strongestValue > 2 or strongestValue2 > 2:
		strongestValue +=1
	hand.append(strongestValue+strongestValue2)
	return hand

def detectOfAKinds(hand):
	strongestValue = 0
	labelChar = ""
	for label in CardLabels: # For each label within CardLabels
		charCount = hand[0].count(label)
		if charCount == 2:
			strongestValue += 1
		if charCount == 3:
			strongestValue = 3
		if charCount == 4:
			strongestValue = 5
		if charCount == 5:
			#print("Test")
			strongestValue = 6
	hand.append(strongestValue)
	return hand

#Read lines of file
#file_path = 'AOC071223input.txt'
file_path = 'AOC071223sample.txt'
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
			if cL1GrCl2(sub_li[j][0],sub_li[j+1][0]) == True:
				tempo = sub_li[j]
				sub_li[j] = sub_li[j + 1]
				sub_li[j + 1] = tempo
	return sub_li

def sortArrayNew(sub_li): # Sorts the given Array of one type by its char-values
	l = len(sub_li)
	sub_li.sort()
	print("Test "+str(sub_li))
	return sorted(sub_li, key=lambda li: li[0])

def cL1GrCl2(cL1, cL2):
	cL1GrCl2Marker = False
	#print(cL1)
	for c in range(0, len(cL1)):
		if CardLabels.index(cL1[c]) < CardLabels.index(cL2[c]) and cL1GrCl2Marker == False:
			cL1GrCl2Marker = True
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
#250337018: too low
#250410933
#250609767: too high
#250641781: ?
#250799231: ?