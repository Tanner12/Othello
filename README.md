# Othello
My code for the game of Othello

A list of lists represents the game board, where '.' are empty spaces, and pieces are either 'B' or 'W' on the game board. The user is able to select which player they want to start, the size of the game board (more than 3 rows and cols, but less than 17), what player gets the top left starting position, and if the user wants the person with the most pieces on the board to win, or the least.

A player places a piece by specifing the row and column of an empty space. My code checks to make sure that the user enters a valid move by checking if there is an opposing player's piece next to the position they chose. Then it makes sure that the position is able to flip the opposing player's piece by keep going in the direction toward the opposing player's piece until a piece of the current player is landed upon. If unsuccessful, the next coordinate is checked, and if none of the coordinates are valid, my code prints an error message to the console and allows the player to choose again.

Each run through of a successful turn, my code checks to make sure that the game is not over, and checks to make sure the current player has a valid move. If the game is over, a message is printed to the console of the winner, if there is one (if not it prints that a draw has occured), the final game board, and the number of pieces each player has.

My code error checks all user input after the game has been started, but my code assumes the user to enter all of the initial starting information correctly.
