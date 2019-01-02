'''
@author: Tanner Sirota
'''

import OthelloErrors
import copy

class Othello:
    
    def __init__(self, rows, cols, turn):
        '''Takes all the inputs to set the initial values of the game. Creates the game board.'''
        self.rows = rows
        self.cols = cols
        self.turn = turn
        self.board = []
        self.mL = ''
        for row in range(rows):
            toAdd = []
            for col in range(cols):
                toAdd.append('.')
            self.board.append(toAdd)
            
            
    def setPlayerPosition(self, pos):
        '''Sets the user specified player in the top left starting position on the game board. 
        Sets the four initial starting pieces.'''
        midRow, midCol = int(self.rows/2) - 1, int(self.cols/2) - 1
        piece = (pos, "W" if pos == "B" else "B")        
        self.board[midRow][midCol] = piece[0]
        self.board[midRow + 1][midCol + 1] = piece[0]
        self.board[midRow + 1][midCol] = piece[1]
        self.board[midRow][midCol + 1] = piece[1]
        
        
    def setMoreOrLess(self, mL):
        '''Sets how the user wants to win.'''
        self.mL = mL
        
        
    def validMove(self, move):
        '''Has the initial check to see if the position a player has selected is valid. It does this by 
        checking all of the coordinates 1 place away, and to make sure there is at least one piece of the
        opposing player next to the position selected. Then the function returns the list of coordinates
        that satisfy that condition.'''
        checkCoords = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (-1, 0), (0, 1), (1, 0)]
        if move[0] < 0 or move[0] >= self.rows or move[1] < 0 or move[1] >= self.cols:
            raise OthelloErrors.OthelloMoveError("Invalid move. Move is out of range.")
        if self.board[move[0]][move[1]] != ".":
            raise OthelloErrors.OthelloMoveError("Invalid move. Spot already taken.")
        contCheck = []
        for coords in checkCoords:
            if coords[0] + move[0] in (self.rows, -1) or coords[1] + move[1] in (self.cols, -1):
                continue
            if self.board[coords[0] + move[0]][coords[1] + move[1]] not in (self.turn, '.'):
                contCheck.append(coords)
        if contCheck == []:
            raise OthelloErrors.OthelloMoveError("Invalid move. Choose a new location.")
        return contCheck
    
    
    def move(self, move):
        '''Using the list of potentially valid coordinates, this function checks all of the directions
        in the list of coordinates to see if the position has a valid move. If there is at least one valid
        move, the function updates the game board using the player's specified position, and changes players.
        If the move is invalid, the function raises an Othello Move Error, with an error message.'''
        coords = self.validMove(move)
        opp = "W" if self.turn == "B" else "B"
        movePass = False
        for coord in coords:
            row, col = move[0] + coord[0], move[1] + coord[1]
            toChange = []
            while row not in (-1, self.rows) and col not in (-1, self.cols) and self.board[row][col] == opp:
                toChange.append((row, col))
                row += coord[0]
                col += coord[1]
            try:
                if self.board[row][col] == self.turn and row  >= 0 and col >= 0:
                    for piece in toChange:
                        self.board[piece[0]][piece[1]] = self.turn
                    self.board[move[0]][move[1]] = self.turn
                    movePass = True
            except:
                continue
        if movePass == False:
            raise OthelloErrors.OthelloMoveError("Invalid move. Choose a new location.")
        self.switchPlayer()
    
    
    def switchPlayer(self):
        '''This function simply switches the player from B to W or vice versa.'''
        self.turn = "W" if self.turn == "B" else "B"
        
    
    def gameOver(self):
        '''This function checks to see if the the game is over, by seeing if the score adds up
        to the amount of available spots on the board, or if there is no valid move for either player.'''
        score = self.getScore()
        black, white = score[0], score[1]
        if black + white == self.rows * self.cols:
            self.getWinner(score, "Board full. Game is over.\nWinner: ")
        if self.canMove() is False:
            self.switchPlayer()
            if self.canMove() is False:
                self.getWinner(score, "No moves available. Game is over.\nWinner: ")
    
        
    def canMove(self):
        '''This function checks if it is possible for a player to move by simulating a player
        choosing any open location on the current game board. The function returns a bool depending
        on whether there is a valid move or not.'''
        possibleMoves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == ".":
                    possibleMoves.append((row,col))
        for move in possibleMoves:
            try:
                previousBoard = copy.deepcopy(self.board)
                self.move(move)
                self.board = previousBoard
                self.switchPlayer()
                return True
            except OthelloErrors.OthelloMoveError:
                continue
        return False
            
    
    def getScore(self):
        '''This function returns the score of the current game by counting the pieces of each side,
        then returns a tuple of black and white's score.'''
        black, white = 0, 0
        for row in self.board:
            for col in row:
                if col == "B":
                    black += 1
                if col == "W":
                    white += 1
        return (black, white)
    
    
    def getWinner(self, score, message):
        '''This function gets the winner of the game depending on user preferences. After getting
        the winner it prints the score, the board, and raises the Othello game over error.'''
        black, white = score[0], score[1]
        winner = ''
        if self.mL == "M":
            winner = "B" if black > white else "W"
        else:
            winner = "B" if black < white else "W"
        winner = "None" if black == white else winner
        self.printBoard()
        self.printScore()
        raise OthelloErrors.OthelloGameOverError(message + winner)
            
    
    
    def printScore(self):
        '''This function simply gets the score, and prints it to the console.'''
        score = self.getScore()
        black, white = score[0], score[1]
        print("Black:", black, " White:", white)
    
    
    def printBoard(self):
        '''This function prints the game board for the user to see in the console.'''
        for row in self.board:
            toPrint = ""
            for col in row:
                toPrint += col + " "
            print(toPrint)
        print()
    
    
    
    
    
    