#Informations: 
#| is a vertical pipe connecting north and south. => u,d
#- is a horizontal pipe connecting east and west. => l,r
#L is a 90-degree bend connecting north and east. => u,r
#J is a 90-degree bend connecting north and west. => u,l
#7 is a 90-degree bend connecting south and west. => d,l
#F is a 90-degree bend connecting south and east. => d,r

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#Arrays


#Definitions
#Read lines of file
#file_path = currentdir+'\outputManuallyRefinedWithoutMiddle.txt'
file_path = currentdir+'/outputInverted.txt'
#file_path = currentdir+'\InputData\AOC101223sample.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

def readString(Lines):
	PipeMap = []
	for line in Lines: 
		PipeMap.append(line)
	return PipeMap

def countPlus(PMap):
	plusCounter = 0
	for n in range(0, len(PMap)): 
		for m in range(0, len(PMap[n])):
			if PMap[n][m] == "+":
				plusCounter += 1
	return plusCounter

print("Number of Plus = "+str(countPlus(readString(Lines))))

#758 is too high
#701 is too high
#600 is too high
#400 is not right