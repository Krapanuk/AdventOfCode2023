
#Arrays
numbersString = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Definitions
def indexes(iterable, obj):
	return (index for index, elem in enumerate(iterable) if elem == obj)

#Read lines of file
file_path = 'AOC011223input.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()
lineCount = 0
for line in Lines:
	lineCount += 1 #print("Line{}: {}".format(count, line.strip()))
	numberCount = 0
	for number in Numbers:
		idxs = indexes(line, number)
		print("Number "+number+ " appears in line "+line+" at position(s) "+str(list(idxs)))
		lineCount += 1