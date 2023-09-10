import random

#Global Variables that will be accessed by multiple functions and used throughout the script
gridSize = 10
shipSymbols = ["B", "S", "D", "C", "M", "O"]
shipNames = ["BattleShip", "SubMarine", "Destroyer", "Carrier", "Mine", "Oyster"]
shipSizes = [4, 3, 2, 5, 1, 1]
shipstoDown = ["BattleShip", "SubMarine", "Destroyer", "Carrier"]
rowCordinates = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
colCordinates = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
gamePlay = True

#function to create the board with the ships placed randomly and is hidden from the player
def createTheBoard():

    # Define the headings for the columns
    headings = [""] + [chr(i) for i in range(ord("A"), ord("A") + gridSize)]

    grid = [["-" for _ in range(gridSize)] for _ in range(gridSize)]

    # Define the ships and their sizes
    ships = {"BATTLESHIP": 4, "SUBMARINE": 3, "DESTROYER": 2, "CARRIER": 5, "MINE": 1, "OYSTER":1}

    # Place the ships randomly on the grid
    for shipName, shipSize in ships.items():
        while True:
            # Choose a random starting position and direction for the ship
            row = random.randint(0, gridSize - 1)
            col = random.randint(0, gridSize - 1)
            direction = random.choice(["horizontal", "vertical"])

            # Check if the ship fits in the chosen position and direction
            if direction == "horizontal" and col + shipSize <= gridSize:
                if all(grid[row][col + i] == "-" for i in range(shipSize)):
                    for i in range(shipSize):
                        grid[row][col + i] = shipName[0]
                    break
            elif direction == "vertical" and row + shipSize <= gridSize:
                if all(grid[row + i][col] == "-" for i in range(shipSize)):
                    for i in range(shipSize):
                        grid[row + i][col] = shipName[0]
                    break
    return grid

# Create the empty ocean as seen by the player
def createOcean(limits):
    ocean = []
    for i in range(limits):
        row = []
        for j in range(limits):
            row.append('-')
        ocean.append(row)
    return ocean

#function to convert the alphanumeric (A0, C5...) cordinates to numeric cordinates
def convertAlphaToNum(shot):
    coordinates = []
    coordinates.append(int(shot[1]))
    number = ord(shot[0]) - ord('A')
    coordinates.append(int(number))
    return coordinates

# function to check if the Missile is a hit or miss
def hitOrMiss(shot, ships):
    results = []
    coordinates = convertAlphaToNum(shot)
    target = ships[coordinates[0]][coordinates[1]]
    if target == 'M':
        results = ["M", "You hit the Mine! Game Over!"]
    elif target == 'O':
        results = ["O", "You found the Oyster, Bot revives a Random Ship!"]
    elif target == 'B':
        results = ["B", "You hit the BattleShip!"]
    elif target == 'S':
        results = ["S", "You hit the SubMarine!"]
    elif target == 'C':
        results = ["C", "You hit the Carrier!"]
    elif target == 'D':
        results = ["D", "You hit the Destroyer!"]
    else:
        results = ["X", "You Missed!"]
    return results

# function to find all the positions of a particular ship
def findPos(ship, map):
    allPos = []
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == ship:
                allPos.append([i,j])
    return allPos

# function to update the ocean with the result of the shot taken
def updateOcean(shot, result, map):
    cordinates = convertAlphaToNum(shot)
    map[cordinates[0]][cordinates[1]] = result
    return map

# function to check the status of the ships and see if they are still sailing or not
def checkShipStatus(symbols, ships):
    #if False then the ship is sunk
    status = [False] * len(symbols) 
    for i in range(len(symbols)):
        for row in ships:
            if symbols[i] in row:
                #if True then the ship is still sailing
                status[i] = True 
    return status

# Main Game Play Loop   
print("---------------------------\n"
      "        BATTLESHIP         \n"
      "---------------------------\n")
print(
    "Welcome to Battleship Captain! \n"
    "We have detected enemy ships in the area. \n"
    "Your mission is to sink all the enemy ships before you run out of Missiles! \n"
    "There are 4 types of ships and their Symbol:Missiles required are: \n"
    "Battleship(B:4), SubMarine(S:3), Destroyer(D:2), Carrier(C:5) \n"
    "It is imperative that you do not hit the Mine or the Oyster! \n"
    "If you hit a Mine, you will lose the game instantly! \n"
    "if you hit a Oyster, the enemy will sell it to revive a random ship! \n"
    "But do not worry, the military has been developing new technology to help you! \n"
    "Since this is a prototype technology, it will take some time to charge! \n"
    "You need to fire 10 Missiles before you can use the Sonar Tech! \n"
    "You will be given a limited number of Sonar Tech to help you find the enemy ships or even a Mine or Oyster! \n"
    "You can use the Sonar Tech by typing 'SONAR'/'sonar' when prompted for a shot! \n"
    "Use them wisely! \n"
    "Good Luck Captain! \n"
)

#loop to keep the game going until the player decides to quit
while gamePlay == True:

    #loop to get the difficulty level from the player and avoid any invalid inputs
    while True:
        difficultyLevel = input("Choose your Difficulty Level: Easy(50 Missiles, 3 Sonar)  Medium(40 Missiles, 2 Sonar)  Hard(30 Missiles, 1 Sonar): ").lower()

        if difficultyLevel == "hard":
            missiles = 30
            sonar = 1
            break
        elif difficultyLevel == "medium":
            missiles = 40
            sonar = 2
            break
        elif difficultyLevel == "easy":
            missiles = 50
            sonar = 3
            break
        else:
            print("Please Enter a Valid Option")
    
    #initializing the variables for the game
    currentOcean = createOcean(gridSize)
    shipLocation = createTheBoard()
    shotsTaken = []
    countTurns = 10

    #loop to keep the game going until the player runs out of missiles, hits the Mine or wins the game
    while missiles > 0:

        print("---------------------------")
        print("  " + " ".join(colCordinates))
        for i in range(gridSize):
            print(str(i) + " " + " ".join(currentOcean[i]))
        print("---------------------------\n"
              "Missiles Left: " + str(missiles))
        print("---------------------------\n"
              "Sonar Left: " + str(sonar))
        
        if countTurns > 0:
            print("---------------------------\n"
                "Turns Left for Sonar Charge: " + str(countTurns))
            print("---------------------------\n")
        else:
            print("---------------------------\n"
                "SONAR Ready!!")
            print("---------------------------\n")
        
        #loop to get the Missile Coordinates from the player and avoid any invalid inputs
        #also checks if the player has any Sonar Tech left and if yes, then it allows the player to use it
        while True:
            
            shotTaken = input("Enter Cordinates for the Missile Strike(example: A0 or a0): ").upper()
            if len(shotTaken) != 2 and shotTaken != "SONAR":
                print("Please enter valid Co-ordinates")
            elif shotTaken == "SONAR":
                if sonar > 0 and countTurns == 0:

                    sonar -= 1
                    countTurns = 10
                    ships = {}
                    strToAdd = ""
                    shipsSailing = checkShipStatus(shipSymbols, shipLocation)
                    for i in range(len(shipsSailing)):
                        if shipsSailing[i] == True:
                            ships.update({shipNames[i]:shipSizes[i]})

                    randShip = shipName,shipSize = random.choice(list(ships.items()))
                    totalPos = findPos(shipName[0], shipLocation)
                    for pos in totalPos:
                        if currentOcean[pos[0]][pos[1]] == '-':
                            currentOcean[pos[0]][pos[1]] = shipName[0]
                            strToAdd = colCordinates[pos[1]]+str(pos[0])
                            shotsTaken.append(strToAdd)
                            break
                    if strToAdd != "":
                        print("---------------------------")
                        print("  " + " ".join(colCordinates))
                        for i in range(gridSize):
                            print(str(i) + " " + " ".join(currentOcean[i]))
                        print("---------------------------\n"
                            "Shots Left: " + str(missiles))
                        print("Sonar Used")
                        print("You Found the " + shipName + " at " + strToAdd)
                    else:
                        print("Sonar Failed, No Ships Found")
        
                elif sonar == 0:
                    print("You have already used all your Sonar Tech")
                else:
                    print("You cannot use Sonar Tech yet, wait for the charge to complete")
            elif shotTaken[0] not in colCordinates or shotTaken[1] not in rowCordinates:
                print("Out of Range")
            elif shotTaken in shotsTaken:
                print("You Already Made that Shot, Try Again!!")
            else:
                shotsTaken.append(shotTaken)
                if countTurns > 0:
                    countTurns -= 1
                else:
                    countTurns = 0
                break

        print("---------------------------")

        #function call to check if the Missile shot is a hit or miss and get results
        shotHitOrMiss = hitOrMiss(shotTaken, shipLocation)
        print(shotHitOrMiss[1])
        
        #if the player hits the Mine, the game ends
        if(shotHitOrMiss[0] == "M"):
            missiles = 0
            print("---------------------------")
            break
        
        #if the player hits the Oyster, the game resets a random ship
        if(shotHitOrMiss[0] == "O"):
            #code to reset a ship at random when oyster is hit
            ships = {"BATTLESHIP": 4, "SUBMARINE": 3, "DESTROYER": 2, "CARRIER": 5}
            shipsSailing = checkShipStatus(shipSymbols, shipLocation)
            if False in shipsSailing[0:4]:
                ships = {}
                for i in range(len(shipsSailing)):
                    if shipsSailing[i] == False:
                        ships.update({shipNames[i]:shipSizes[i]})
            randShip = shipName,shipSize = random.choice(list(ships.items()))
                        
            for i in range(gridSize):
                for j in range(gridSize):

                    if currentOcean[i][j] == shipName[0]:
                        currentOcean[i][j] = '-'
                        strToPop = colCordinates[j]+str(i)
                        if strToPop in shotsTaken:       
                            shotsTaken.remove(strToPop)
                    if shipLocation[i][j] == shipName[0]:
                        shipLocation[i][j] = '-'

            while True:

                # Choose a random starting position and direction for the ship
                row = random.randint(0, gridSize - 1)
                col = random.randint(0, gridSize - 1)
                direction = random.choice(["horizontal", "vertical"])

                # Check if the ship fits in the chosen position and direction
                if direction == "horizontal" and col + shipSize <= gridSize:
                    if all(shipLocation[row][col + i] == "-" for i in range(shipSize)):
                        for i in range(shipSize):
                            shipLocation[row][col + i] = shipName[0]
                        break
                elif direction == "vertical" and row + shipSize <= gridSize:
                    if all(shipLocation[row + i][col] == "-" for i in range(shipSize)):
                        for i in range(shipSize):
                            shipLocation[row + i][col] = shipName[0]
                        break
        
        #function call to update the ship location matrix with the result of the shot taken
        shipLocation = updateOcean(shotTaken, "X", shipLocation)

        #function call to check the status of the ships and see if they are still sailing or not
        shipsSailing = checkShipStatus(shipSymbols, shipLocation)
        for i in range(len(shipsSailing)):
            if shipsSailing[i] == True:
                print(shipNames[i] + " is sailing")
            else:
                print(shipNames[i] + " has been taken down!")
        
        #function call to update the ocean with the result of the shot taken
        currentOcean = updateOcean(shotTaken, shotHitOrMiss[0], currentOcean)

        #if all the ships are sunk, the player wins the game
        if True not in shipsSailing[0:4]:
            print("You have defeated the enemy! Congratulations Captain!!")
            break

        missiles -= 1

        #if the player runs out of missiles, the game ends
        if missiles == 0:

            print("You Lost Captain! Here is the Location of the Enemy Ships")
            print("---------------------------")
            print("  " + " ".join(colCordinates))
            for i in range(gridSize):
                print(str(i) + " " + " ".join(shipLocation[i]))
            print("---------------------------\n")
    
    #loop to ask the player if they want to play again or not
    tryAgain = input("Would you like to play again? (Y/N) ").upper()
    if tryAgain == 'Y':
        gamePlay = True
    elif tryAgain == 'N':
            gamePlay = False
            break

print("Just run the command if you want to go again")