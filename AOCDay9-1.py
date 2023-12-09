#Procedure
# 1) Read each line as an array of all numbers within an array of all lines
# 2) To the array for each line append another array with alle differences 
#    a. for all lines within the array: for l in range (0, len(ArrayOfAllLines)):
#       for all values within the first to the last sub-Array: for i in range (1, len(ArrayOfAllLines[l])):
#       calculate des difference: 
#          1stValue = int(ArrayOfAllLines[l][i-1])
#          2ndValue = int(ArrayOfAllLines[l][i])
#          if 1stValue > 2ndValue: difference = 1stValue - 2ndValue
#          else: difference = 2ndValue - 1stValue
#    b. ArrayOfAllLines[LineNr].append[Array of diffs]
