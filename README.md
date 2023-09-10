# Battleship
Welcome to my own custom variation of BattleShip
This game follows the basic rules of Battleship where you have to sink the enemy Battleships by hitting them at desired co-ordinates. However, in this game we have the following rules:

1. There are 3 difficulty Levels: Easy, Medium, Hard and based on difficulty levels you get appropriate power-ups and Missiles to attack

2. There is a power up called 'SONAR' which auto-activates after every 10 turns and can be used to find a random item on the Game Board. The number of Sonar you get varies on the difficulty levels

3. There is 1 MINE hidden in the game board, in case the Mine is hit, its Game Over

4. There is 1 Oyster hidden in the game board, in the event the Oyster is hit, a bot randomly revives a ship and changes the location of the ship on the board. If all ships are sailing it will randomly pick one and re-arrange the location of the ship

Happy Hunting!

(There is also a bonus [flowchart](https://github.com/architg07/Battleship/blob/main/Battleship%20Flowchart.png) in the repo which provides the basic flow of the game.)

To run the game there are a couple of options:

1. A docker repo has been created and the following steps can be taken to run it:

    Pull the Docker Image:
   ```docker pull architg07/my-battleship-image```

    Run the Docker Image in Interactive Mode:
   ```docker run -i architg07/my-battleship-image```

2. In the event running Docker on a local setup is not a permissible operation,the repo can be cloned and running the "Battleship.py" file will run the game in the terminal. 
