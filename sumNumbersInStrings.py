
#Arrays
numbersString = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberDigit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Read lines of file
file_path = 'AOC_011223_StringData.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()
lineCount = 0
for line in Lines:
    	lineCount += 1
    	#print("Line{}: {}".format(count, line.strip()))
    	numberCount = 0
	for number in Numbers:
		indexes = indexes(line, number)
      		print("Number "+number+ " appears in line "+line+" at position(s) "+list(indexes))
		lineCount += 1
