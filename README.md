The object of MASTERMIND (r) is to guess a secret code consisting of a series of 4
colored pegs. Each guest results in feedback narrowing down the possibilities of the
code. The winner is the player who solves his opponent's secret code with fewer
guesses. This program is supposed to solve the opponent's secret code with fewer guesses 
as possible. His enemy will be the programmer that will be inputting the pins.

There are 7 colors that the programmer can choose to make the password, but he cannot
repeat any color (the order of the color matters). Each collor wil be assigned with a letter
Y - Yellow
R - Red
B - Blue
G - Green
O - Orange
P - Purple
k - Pink

For each guess, the program will ask how many white and black pins it got for that password,
the white pin represent a pin that its color is in the real password, but it's not in the 
exact position.
The black pin represent a pin that its color and position exactly match with the real password.

Example: Real password BGOY

Guess 1 - PRBG (2 white pins - 0 black pins)
Guess 2 - OBGY (3 white pins - 1 black pin)
Guess 3 - BGOY ( 0 white pins - 4 black pins)  - password correct


*The programmer must enter the correct input, so it follow the rules of the game and the logic of the program.
