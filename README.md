# Snake And Ladder Application
A python based application which works on CLI to function like the coventional snake and ladder game.
  
## Contents
* Snake and Ladder Application
* Contents
* Technologies Required
* About Code
* How to Use
* Methods Defined
* Program Description
* Bibliography

## Technologies Required
Project is created using:
* Python: 3.8.6
* Flake8 (for liniting)
* Visual Studio Code IDE

## About Code
The application has been coded in python language using OOPS principle having objects and methods running with some user provided data.

## How To Use
* Open and run the code in any python IDE.
* Provide the user inputs like snakes' details, ladders, detail and players' names.
* Now just simply follow the commands in terminal and the game will go on smoothly until one player wins the game.

## Methods Defined
* start_game()
* roll_a_dice()
* check_ladder()
* check_snake()
* move_calculator()
* check_win()

## Program Description
* The program stores the position of ladders and snakes in a dictionary and the player names and their position in game in a nested list.
* When the dice is rolled, the dice value is obtained from roll_a_dice() function and is added to the old position of player.
* This new position is checked in the user provided snakes and ladders dictionaries by the funtions check_ladder() and check_snake(); and if found then the player's position is again updated according to the data in the dictionaries.
* The program sleeps for 1 second before giving the next update on terminal for a smooth user experience.
* The game is played until one player's postion becomes equal to 100, thereby declaring him/her the winner.

## Bibliography
The following sources were found to be of help :
> tutorialspoint.com  
> w3schools.com  
> Head First Python by Paul Barry  
