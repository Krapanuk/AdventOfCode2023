#Arrays
CubeColoursString = [ "red", "green", "blue"]
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
			startPos = charCount
		charCount += 1
	subGamesInGame.append(game[startPos:charCount])
	return subGamesInGame

def extractNumberOfCubes(colourString):

	cleanedString = colourString.replace(" ","").replace(":","").replace(";","").replace(",","").replace("green","").replace("red","").replace("blue","")
	return int(cleanedString)

#Read lines of file
file_path = 'AOC021223input.txt'
with open(file_path, 'r', encoding='utf-8') as file:
	Lines = file.readlines()

#One Line per Game: Cut out Subgames
gameNumber = 1
colourCount = 0
sumPowers = 0
for line in Lines:
	minCubeNumbers = [0, 0, 0]
	gamePossible = 1
	coloursInSubgame = []
	subGameCount = 0
	for subGame in cutSubgames(line, ";"):
		gameColourCount = 0
		for colours in cutSubgames(subGame, ","): # For every colour in given SubGame
			colourCount = 0
			for colour in CubeColoursString: # For every possible colour
				if cutSubgames(subGame, ",")[gameColourCount].find(colour) > 0: # If the given colour exists as colour within the SubGame
					if extractNumberOfCubes(cutSubgames(subGame, ",")[gameColourCount]) > minCubeNumbers[colourCount]:
						minCubeNumbers[colourCount]	= extractNumberOfCubes(cutSubgames(subGame, ",")[gameColourCount])				
				colourCount += 1
			gameColourCount += 1
		subGameCount += 1
	power = minCubeNumbers[0] * minCubeNumbers[1] * minCubeNumbers[2]
	print("Game "+str(gameNumber)+": Min. required Cubes "+str(minCubeNumbers)+ "[Power:"+str(power)+"]")
	sumPowers = sumPowers + power
	gameNumber += 1
print("Sum: "+str(sumPowers))