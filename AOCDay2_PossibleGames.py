#Arrays
CubeColoursString = [ "red", "green", "blue"]
CubeNumbers = [12, 13, 14]
sumGameIDs = 0

#Definitions
def cutSubgames(game, delimiter):
	subGamesInGame = []
	startPos = 0
	endPos = 0
	charCount = 0
	for character in game:
		if character == ":":
			startPos = charCount			
		if character == delimiter:
			endPos = charCount
			subGamesInGame.append(game[startPos:endPos])
			#print(game[startPos:endPos])
			startPos = charCount
		charCount += 1
	subGamesInGame.append(game[startPos:charCount])
	#print(game[startPos:endPos])
	return subGamesInGame

def extractNumberOfCubes(colourString):
	#print("> extractNumberOfCubes:"+colourString)
	cleanedString = colourString.replace(" ","").replace(":","").replace(";","").replace(",","").replace("green","").replace("red","").replace("blue","")
	#print("> extractNumberOfCubes: Number: "+cleanedString)
	return int(cleanedString)

#Read lines of file
file_path = 'AOC021223input.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

#One Line per Game: Cut out Subgames
gameNumber = 1
colourCount = 0
for line in Lines:
	gamePossible = 1
	#print("Game "+str(gameNumber)+": "+str(cutSubgames(line, ";")))
	coloursInSubgame = []
	subGameCount = 0
	for subGame in cutSubgames(line, ";"):
		#print("With Subgames: "+str(cutSubgames(subGame, ",")))
		gameColourCount = 0
		for colours in cutSubgames(subGame, ","): # For every colour in given SubGame
			colourCount = 0
			for colour in CubeColoursString: # For every possible colour
				if cutSubgames(subGame, ",")[gameColourCount].find(colour) > 0: # If the given colour exists as colour within the SubGame
					if extractNumberOfCubes(cutSubgames(subGame, ",")[gameColourCount]) > CubeNumbers[colourCount]:
						if gamePossible > 0:
							print("Game "+str(gameNumber)+" Impossible: Within SubGame "+str(subGameCount)+" for Colour "+colour+" the max. Value of " +str(CubeNumbers[colourCount])+ " is exceeded ["+str(extractNumberOfCubes(cutSubgames(subGame, ",")[gameColourCount]))+"]!")
							gamePossible = 0 # Game impossible						
				colourCount += 1
			gameColourCount += 1
		subGameCount += 1
	if gamePossible > 0:
		print("Game "+str(gameNumber)+" Possible!")
		sumGameIDs = sumGameIDs + gameNumber
	gameNumber += 1
print("Sum: "+str(sumGameIDs))