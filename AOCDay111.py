import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#Arrays
SpaceWithoutExpansion = [] # All pipe positions
Space = []

#Definitions
#Read lines of file
#file_path = 'AOC101223input.txt'
file_path = currentdir+'/InputData/AOC111223sample.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

def readString(Lines):
	for line in Lines: 
		SpaceWithoutExpansion.append(line)
	return SpaceWithoutExpansion

def expand1(SpaceWithoutExpansion):
	Expanded = []
	lineCount = 0
	for line in SpaceWithoutExpansion:
		lineCount += 1
		Expanded.append(line)
		if line.find("#") == -1:
			lineCount += 1
			Expanded.append(line)
	containsHash = False
	for charPos in range(0, len(SpaceWithoutExpansion[0])-1):
		LineArray = []
		for lineNr in range (0,len(SpaceWithoutExpansion)):
			if SpaceWithoutExpansion[lineNr][charPos] == "#":
				print("LineNr["+str(lineNr)+"] CharPos["+str(charPos)+"]" +SpaceWithoutExpansion[lineNr][charPos])
				containsHash = True
			else: containsHash = False
		if containsHash == False:
			print("Column ["+str(charPos)+"] without #")
			for lineNr in range (0,lineCount):
				Expanded[lineNr] = Expanded[lineNr][:charPos] +"."+ Expanded[lineNr][charPos:]
				#Expanded[lineNr][charPos] = ".."
	writeToFile(Expanded,"AOC111223Output.txt")
	return Expanded


def addLinesAndColumns(PArray):
	addedArray = []
	for n in range(0, len(PArray)): # Add new empty line at every second line
		Line = []
		EmptyLine = []
		for m in range(0, len(PArray[n])):
			Line.append(PArray[n][m])
			Line.append('*')
			EmptyLine.append('*')
			EmptyLine.append('*')
		addedArray.append(Line)
		addedArray.append(EmptyLine)	
	return connectPipes(addedArray)

def expand(SpaceWithoutExpansion):
	AddedArray = []
	for line in range(0, len(SpaceWithoutExpansion)):
		Line = []
		for char in range(0, len(SpaceWithoutExpansion[line])):
			Line.append(SpaceWithoutExpansion[line][char])
			if hashInColumn == False:
				Line.append(".")
		AddedArray.append(Line)
	for charPos in range(0, len(SpaceWithoutExpansion[0])-1):
		LineArray = []
		for lineNr in range (0,len(SpaceWithoutExpansion)):
			if SpaceWithoutExpansion[lineNr][charPos] == "#":
				print("LineNr["+str(lineNr)+"] CharPos["+str(charPos)+"]" +SpaceWithoutExpansion[lineNr][charPos])
				containsHash = True
			else: containsHash = False
		if containsHash == False:
			print("Column ["+str(charPos)+"] without #")
			for lineNr in range (0,lineCount):
				Expanded[lineNr] = Expanded[lineNr][:charPos] +"."+ Expanded[lineNr][charPos:]
				#Expanded[lineNr][charPos] = ".."
	writeToFile(Expanded,"AOC111223Output.txt")
	return Expanded

def hashInLine(SpaceWithoutExpansion, line):
	hInLine = False
	for char in range(0, len(SpaceWithoutExpansion[line])):
		if SpaceWithoutExpansion[line][char] == "#":
			hInLine = True
	return hInLine

def hashInColumn(SpaceWithoutExpansion, char):
	hInColumn = False
	for line in range(0, len(SpaceWithoutExpansion)):
		if SpaceWithoutExpansion[line][char] == "#":
			hInColumn = True
	return hInColumn

def writeToFile(PArray, filename):
	with open(filename, "w") as txt_file:
		for line in PArray:
			txt_file.write("".join(line))

print("Expanded = "+str(expand(readString(Lines))))

#Result: 