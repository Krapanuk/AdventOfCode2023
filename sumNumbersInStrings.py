
#Arrays
NumbersString = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NumbersDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
	numberStringCount = 0
	print("Oringinal String: "+line)
	new_string = line
	for numberString in NumbersString:
		new_string = new_string.replace(numberString, NumbersDigit[numberStringCount])
		numberStringCount += 1
	print("New String: "+ new_string)
	numberCount = 0
	numbersInLine = []
	for number in NumbersDigit:
		idxs = indexes(new_string, number)
		numbersInLine.append(list(idxs))
		lineCount += 1
	print("Numbers in line "+new_string+" at position(s) "+str(numbersInLine))