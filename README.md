# READ ME
### Battleship Game

![Battleship Game](assets/images/screenshotBattleshipGame.png)

## Overview
This Battleship Game is a command-line game written in Python. Two players, one controlled by the user and the other by the computer, take turns guessing the location of the opponent's ships on a grid. The game dynamically updates the board based on the players' guesses and provides feedback on hits and misses.

## Features
- **Dynamic Ship Placement:** Ships are randomly placed on the board with varying sizes and orientations (horizontal or vertical), making each game unique.
- **Turn-based Gameplay:** Players take turns guessing the coordinates of the opponent's ships. The game provides feedback for each guess, indicating whether it was a hit or a miss.
- **Winning Condition:** The game tracks the number of ships remaining and ends when all ships of one player have been sunk.
- **Input Validation:** Ensures that player guesses are within the grid bounds and are entered in the correct format.

## Usage
To play the game, simply run the script. The user will be prompted to enter the grid size, and then the game will begin. Players take turns guessing the row and column where they believe a ship is located. The board will update accordingly, and the game will continue until one player has sunk all the opponent's ships.

## Content
- **Dynamic Grid:** The game board is created based on the user-defined size, ensuring a customizable playing experience.
- **Ship Placement:** Ships are placed randomly on the board, with varying sizes and directions.
- **Player and Computer Turns:** Both the player and the computer take turns guessing ship locations, with the results displayed after each guess.
- **End Game Condition:** The game ends when one player sinks all the opponent's ships, with a message displayed indicating the winner.

### Testing
The game was tested to ensure that ships are placed correctly, guesses are validated properly, and the game ends when all ships are sunk.

### Functionality Testing
The following table summarizes the testing of the main functionalities of the Battleship Game:

| Functionality                   | Expected Outcome                                | Result          |
|---------------------------------|--------------------------------------------------|-----------------|
| Ship Placement                  | Ships are placed randomly on the board           | Pass            |
| Player Guess                    | Guess is validated and board updates accordingly | Pass            |
| Computer Guess                  | Computer's guess is within bounds and updates board | Pass          |
| End Game Condition              | Game ends when all ships of one player are sunk  | Pass            |

### Additional Testing
- **Python Code Validation** using [PEP8 online](http://pep8online.com/)
  - Fixed indentation and spacing issues to comply with PEP8 standards.

- **User Input Validation** 
  - Tested various inputs (out of bounds, non-integer values) to ensure robust handling.

- **Game Playthrough** 
  - Played multiple rounds to verify the random placement of ships and the integrity of the game logic.

## Deployment
The site was deployed to GitHub Pages. The steps to deploy are as follows:
1. In the GitHub repository, navigate to the **Settings** tab.
2. From the source section drop-down menu, select the **Master Branch**.
3. Once the master branch has been selected, the page will automatically refresh with a detailed ribbon display to indicate the successful deployment.

This deployment was deployed using the Code institutes mock terminal for **Heroku**.

Steps for deployment:
  1. Fork or clone this repository
  
  2. Create a new heroku app
  3. Set the buildpacks to python and node.js in that order 
  4. Link the heroku app to the repository
  5.  Click on deploy


  ## Credits

  - The README structure and layout were adapted from a previous example focused on a web-based Dice Game.
  - The deployment section to github in README.md is from  [This README example](https://github.com/Code-Institute-Solutions/readme-love-maths/blob/master/README.md)
