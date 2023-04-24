# Othello / Reversi

This project was made in late December 2023 as coding practice after I finished my finals. The code consists of two main parts: the game's boilerplate, and the computer, including a basic user visualization and interface as well.

## Basic rules

Othello / Reversi is a two player game where each player starts with two checkers in the middle of the board and places one checker each turn of his/her color. After each person places their token, any tokens encapsulated by the same color get flipped to that color. The game ends when a play either flips over all their opponent's pieces or there are no available spaces, at which point the player with more tokens of their color wins

## How to play

After opening `Othello.py`, the user will be greeted with a simple interface to gather parameters for the game. After the user enters the information to the program, they will see the board visualized with X's for one player and O's for the other. To play a move, type for coordinates of the point and the current player's token will go in that location. When a play wins, the program will display the results

## Features

- The user may increase the board size by inputting an even integer, if he/she wishes not to, press enter to accept the default: 8
- The game may be played with 0-2 players, if a computer is used (0 or 1 players) the type of computer can be defined in the `Othello.py` file
- Pause time is helpful in watching two computers play each other at a rapid pace. Press enter to accept the default (0ms)

- During play with computers, the program will print the computer's gain, which is a computation based on a rudimentary scoring system for the current game state where 1.00 indicates 100% X's pieces and -1.00 represents 100% O's pieces
- After the game finished, a plot will appear that shows the score every move (2 ply) during the game

## Future

At the moment, my main goal for the future is to use some sort of reinforcement learning to develop and train a model to play the game based on the game rules written. I am currently learning how to use Tensorflow/Keras and hope to accomplish this in the coming months.
