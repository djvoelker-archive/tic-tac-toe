'''
Created on Aug 21, 2021

@author: djvoe

Things to add:
    - GUI
    - Error handling when input isn't an integer between 1 - 9
    - Not have computer respond instantly
    - Not print out different board for each move
    - Choose who goes first and who plays as X and who plays as O
'''

from operator import itemgetter
from random import randint
from time import sleep


class game:
    def __init__(self):
        self.grid = [x+1 for x in range(9)]
        self.print_grid()
        self.setup_grid()
        self.winner = False
        self.exit = False
        self.turns_played = 0
        while self.winner == False:
            self.player_turn()
            if self.exit == True:
                game.exit = True
                return
        self.print_grid()
        print(self.winner)


    def setup_grid(self):
        self.grid = [" " for _ in range(9)]
        
        
    def print_grid(self):
        print("\n")
        for r in range(3):    
            print("     " + str(self.grid[3*r+0]) + " | " + str(self.grid[3*r+1]) + " | " + str(self.grid[3*r+2]))
            if r < 2: print("    -----------")
        print("\n\n------------------------------------------------------------")
        
        
    def player_turn(self):
        player_sel = input("\n What box (from 1 - 9) would you like to draw an X in? ")
        if player_sel.casefold() == "exit": self.exit = True
        try:
            if self.grid[int(player_sel)-1] == " ":
                
                #player turn
                self.grid[int(player_sel)-1] = "X"
                self.winner = self.check_for_winner('X')
                if self.winner == 'X': 
                    self.winner = " You win!"
                    return
                elif self.winner == " The game is a tie.":
                    return
                self.turns_played += 1
                
                #computer turn        
                self.scan_board('O')
                self.winner = self.check_for_winner('O')
                if self.winner == 'O': 
                    self.winner = " You lose!"
                    return
                elif self.winner == " The game is a tie.":
                    return
                self.turns_played += 1
                
                self.print_grid()
                
            else: print("\n That space is already filled in!\n")
        
        except (ValueError, IndexError):
            print("\n Please type an integer from 1 - 9 or type 'exit' to exit game.")
        
        
    def scan_board(self, a):
        #check diagonals
        if (itemgetter(0,8)(self.grid) == (a, a) and self.grid[4] == " ") or (itemgetter(2,6)(self.grid) == (a, a) and self.grid[4] == " "):
            self.grid[4] = 'O'
            return
        if itemgetter(4,8)(self.grid) == (a, a) and self.grid[0] == " ":
            self.grid[0] = 'O'
            return
        if itemgetter(4,6)(self.grid) == (a, a) and self.grid[2] == " ":
            self.grid[2] = 'O'
            return
        if itemgetter(2,4)(self.grid) == (a, a) and self.grid[6] == " ":
            self.grid[6] = 'O'
            return
        if itemgetter(0,4)(self.grid) == (a, a) and self.grid[8] == " ":
            self.grid[8] = 'O'
            return
        
        #check rows
        for r in range(3):
            if itemgetter(3*r, 3*r+1)(self.grid) == (a, a) and self.grid[3*r+2] == " ":
                self.grid[3*r+2] = 'O'
                return
            if itemgetter(3*r+1, 3*r+2)(self.grid) == (a, a) and self.grid[3*r] == " ":
                self.grid[3*r] = 'O'
                return
            if itemgetter(3*r, 3*r+2)(self.grid) == (a, a) and self.grid[3*r+1] == " ":
                self.grid[3*r+1] = 'O'
                return
        
        #check columns
        for c in range(3):
            if itemgetter(c, 3+c)(self.grid) == (a, a) and self.grid[6+c] == " ":
                self.grid[6+c] = 'O'
                return
            if itemgetter(3+c, 6+c)(self.grid) == (a, a) and self.grid[c] == " ":
                self.grid[c] = 'O'
                return
            if itemgetter(c, 6+c)(self.grid) == (a, a) and self.grid[3+c] == " ":
                self.grid[3+c] = 'O'
                return
        
        #fill in random spot if there is no opportunity to block player
        if a == 'X':
            squares = [x for x in range(9)]
            while True:
                n = randint(0,len(squares)-1)
                if self.grid[squares[n]] == " ":
                    self.grid[squares[n]] = 'O'
                    return
                del squares[n]
        
        #if no opportunity for computer to win, it will then see if the player has an opportunity to win and will block them.
        #if the player does not have the opportunity to win, the computer will then place an O at a random empty spot on the board.
        self.scan_board('X')
    
    
    def check_for_winner(self, x):
        if (
                itemgetter(0,1,2)(self.grid) == (x, x, x)
                or itemgetter(3,4,5)(self.grid) == (x, x, x)
                or itemgetter(6,7,8)(self.grid) == (x, x, x)
                or itemgetter(6,7,8)(self.grid) == (x, x, x)
                or itemgetter(0,3,6)(self.grid) == (x, x, x)
                or itemgetter(1,4,7)(self.grid) == (x, x, x)
                or itemgetter(2,5,8)(self.grid) == (x, x, x)
                or itemgetter(0,4,8)(self.grid) == (x, x, x)
                or itemgetter(2,4,6)(self.grid) == (x, x, x)
            ):
            return x
        elif self.turns_played > 7: return " The game is a tie."
        else: return False


def play_tic_tac_toe():
    game.exit = False
    print(" Welcome to Tic-Tac-Toe. Type 'exit' to exit game.")
    game()
    if game.exit == True:
        print("\n Exiting game . . . ")
        sleep(2)
        return
    while True:
        sleep(2)
        p = str(input("\nPlay again? Y/N: ")).casefold()
        if p == "y":
            print("\n\n")
            game()
        elif p == "n" or p == "exit":
            print("\n Exiting game . . . ")
            sleep(2)
            return
        else: print("\nPlease type Y/N.")


play_tic_tac_toe()

