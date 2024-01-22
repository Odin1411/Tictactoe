# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:24:40 2024

@author: olivi
"""
from Tictactoe import Tictactoe 
from Tictactoe import Computer
import random as rand

positions = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}

class Game(Tictactoe):
    def __init__(self, startplayer=1,difficulty =1):
        '''
        Parameters
       ----------
       gamedict : dict
           current board
       startplayer : int
           1 is player, 2 is computer
       movesmade : int
           keeps track of how many moves have been made
       winner : 
           can be None, 1,2 or "draw"
       prevturn: int
           keeps track of who made previous move
        ''' 
        super().__init__()
        board = Tictactoe()
        self.computer = Computer(difficulty,2)
        self.gamedict = board.gamedict
        self.size = len(self.gamedict)
        self.startplayer = startplayer
        self.movesmade= 0
        self.winner = None
        self.currentturn = startplayer
        
    def move_player(self,position):
        self.update_gamedict(position, 1)
        self.movesmade = self.movesmade +1
        

    def move_computer(self):
        computer = self.computer
        print(f'difficulty {computer.difficulty}')
        if computer.difficulty == 0:
            move = computer.strategy0(self)
        elif computer.difficulty == 0.5:
            move = computer.strategy0_5(self)
        elif computer.difficulty == 1:
            move = computer.strategy1(self)
        elif computer.difficulty == 2: 
            move = computer.strategy2(self)
            
        
        if not move and not self.winner:
            raise Exception("Something went wrong")
        
        if move:
            self.update_gamedict(move,2)
            self.movesmade = self.movesmade +1
        
    #def set_turn(self):
    #    if self.movesmade == 0:
    #        current_turn = self.startplayer
    #    else:
    #        if self.prevturn == 1:
     #           current_turn = 2
     #       elif self.prevturn == 2:
    #            current_turn = 1
        
    #    return current_turn
    
    def set_turn(self,num):
        self.currentturn = num
    
    def get_turn(self):
        return self.currentturn
                         

    def end_of_game(self,difficulty):
        '''
        return empty game if play again. return none if not
        '''
        if self.winner == 2:
            print("Game over. You lost")
        elif self.winner == 1:
            print("Congratulations! You won.")
        else:
            print("it's a draw!")
        while True:              
            play = input("Want to play again? [Yes/No] ") 
            if play.lower() == "no":
                print("thanks for playing! Goodbye")
                return None
    
            if play.lower() == "yes":
                new_game = Game(1,difficulty)
                print(new_game)
                return new_game
            else: print("??") 
            



def handle_input(game,player_choice):
    player_choice = int(player_choice)
    pos = positions[player_choice]
    game.move_player(pos)
    

def random_startplayer():
    ''' 
    return 1 (player) or 2 (computer)
    '''
    randomint = rand.randint(1,2)
    return randomint    

def intro_text(game):
    print("Welcome to tictactoe!")   
    print(game)
             
def gameloop():
    #startplayer = random_startplayer()
    startplayer = 1
    difficulty = 0.5
    game = Game(startplayer,difficulty)
    intro_text(game)
    exitloop = False
    while not exitloop:
        
        winner = game.check_win()
        if winner:
            game = game.end_of_game(difficulty)
            if game:
                continue
            return
            
        current_turn = game.get_turn()
        print(current_turn)
        if current_turn == 2:
            game.move_computer()
            game.set_turn(1)
            print("computer has made a move")
        elif current_turn == 1:
        
            while True:
                player_choice = input("Choose an empty slot: ")
                
                if player_choice == "exit" or player_choice == "quit":
                    return
                
                try: 
                    player_choice = int(player_choice)
                    if player_choice not in positions:
                        print("Not a valid input")
                        print(game)
                        continue
                
                    pos = positions[player_choice]
                    game.move_player(pos)
                    game.set_turn(2)
                    break
                except ValueError:
                    print("please choose a number between 1-9")
                    print(game)
                except Exception as e:
                    print(e)
                    print(game)
            
        
            
        print(game) 
        
if __name__ == "__main__"  :      
    gameloop()        
        
        
            
             
