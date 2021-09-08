'''
Created on Aug 21, 2021

@author: djvoe

Things to add:
    - GUI
    - Not have computer respond instantly
    - Not print out different board for each move
    - Choose who goes first and who plays as X and who plays as O
'''

from random import randint
from time import sleep


class game:
    exit = False
    def __init__(self):
        self.grid = [x+1 for x in range(9)]
        self.print_grid()
        self.setup_grid()
        self.winner = False
        self.exit = False
        self.turns_played = 0
        while self.winner == False:
            self.take_turns()
            if self.exit == True:
                game.exit = True
                return
        print("\n" + self.winner)

    def setup_grid(self):
        self.grid = [" " for _ in range(9)]
            
    def print_grid(self):
        print("\n")
        for r in range(3):    
            print("     " + str(self.grid[3*r+0]) + " | " + str(self.grid[3*r+1]) + " | " + str(self.grid[3*r+2]))
            if r < 2: print("    -----------")
        print("\n\n------------------------------------------------------------")
        
    def take_turns(self):
        player_sel = input("\n What box (from 1 - 9) would you like to draw an X in? ")
        if player_sel.casefold() == "exit":
            self.exit = True
            return
        elif player_sel.casefold() != "exit":
            try:    
                if self.grid[int(player_sel)-1] == " ":
                    #player turn
                    self.grid[int(player_sel)-1] = "X"
                    self.check_win_or_tie('X', 'O')
                    if self.winner == " The game is a tie.": return
                    #computer turn
                    self.scan_board('O','O', False)
                    self.check_win_or_tie('O', 'X')
                    if self.winner == " The game is a tie.": return                    
                    
                    self.print_grid()
                    
                else: print("\n That space is already filled in!\n")
            
            except ValueError:
                self.grid[int(player_sel)-1] = " "
                print("\n Please type an integer from 1 - 9 or type 'exit' to exit game.")
            except IndexError: print("\n Please type an integer from 1 - 9 or type 'exit' to exit game.")
    
    def scan_board(self, i, j, check_win):
        for m in range(3):
            for n in range([2,3,3][m]):
                a = [self.grid[[2*n+2*(2-n)*x, 3*n+x, n+3*x][m]] for x in range(3) if self.grid[[2*n+2*(2-n)*x, 3*n+x, n+3*x][m]] == i]
                g = [self.grid[[2*n+2*(2-n)*x, 3*n+x, n+3*x][m]] for x in range(3)]
                if (check_win == True):
                    if (i in g) and (len(set(a)) < (len(a)-1)) and (' ' not in g) and (j not in g):
                        self.winner = i
                        return
                elif (check_win == False) and (i in g) and (' ' in g) and (len(set(a)) < len(a)):
                    self.grid[[2*n+2*(2-n)*g.index(" "), 3*n+g.index(" "), n+3*g.index(" ")][m]] = j
                    return
                
        if (i,j,check_win) == ('O','O',False): self.scan_board('X','O',False)
        elif (i,j,check_win) == ('X','O',False):
            squares = [x for x in range(9)]
            while True:
                n = randint(0,len(squares)-1)
                if self.grid[squares[n]] == " ":
                    self.grid[squares[n]] = 'O'
                    return
                del squares[n]
    
    def check_win_or_tie(self, i, j):
        if self.turns_played > 3:
            self.scan_board(i, j, True)
            if self.winner == i: 
                if i == 'O':
                    self.winner = " You lose!"
                else:
                    self.winner = " You win!"
                return
            elif self.winner == " The game is a tie.":
                return
                        
        self.turns_played += 1
                    
        if " " not in self.grid:
            self.winner = " The game is a tie."
            return


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
        p = str(input("\n Play again? Y/N: ")).casefold()
        if p == "y":
            print("\n")
            game()
        elif p == "n" or p == "exit":
            print("\n Exiting game . . . ")
            sleep(2)
            return
        else: print("\n Please type Y/N.")


play_tic_tac_toe()

