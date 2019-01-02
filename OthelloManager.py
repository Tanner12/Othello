'''
@author: Tanner Sirota
'''


import Othello
import OthelloErrors

if __name__ == '__main__':
    game = Othello.Othello(int(input("Enter the number of rows (4-16):  ")), int(input("Enter the number of columns (4-16):  ")), input("Enter the starting player (B or W):  ").upper())
    game.setPlayerPosition(input("Enter the player that will go in the top left corner (B or W):  ").upper())
    game.setMoreOrLess(input("Enter the winning type to be the most or least pieces (M or L):  ").upper())
    game.printScore()
    print("Turn:  " + game.turn)
    game.printBoard()
    while True:
        try:
            move = int(input("Enter the row:  ")) - 1, int(input("Enter the column:  ")) - 1
            print()
            game.move(move)
            game.gameOver()
            game.printScore()
            game.printBoard()
            print("Turn:  " + game.turn)
        except OthelloErrors.OthelloMoveError as e:
            print(e, '\n')
        except OthelloErrors.OthelloGameOverError as e:
            print(e)
            break
        except ValueError:
            print("\nThe row and column must be valid positive integers.\n")
    