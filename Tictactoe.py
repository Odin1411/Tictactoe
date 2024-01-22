# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:57:24 2022

@author: olivi
"""

import random as rand
import matplotlib.pyplot as plt
#tiktaktoe 
#|0 |1 | 2| 0 är granne med alla utom 7 och 5
#|3 |4 | 5| 5 är granne med alla utom 0 1 6 och 7 
#|6 |7 | 8| 4 är granne med alla 

positions = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}

def initialize_dict(size=3):
    return{i : None for i in range(size*size)}
        
   
class BoardPosition:
    """class for a position on the board
    
    """
    def __init__(self,position):
        """
        Parameters:
            occupied_by (int): None, 1 or 2
            name (str):  probably not necessary anymore
            position (tuple): position on board
        """
        self.occupied_by = None
        self.name = self.setName(position)
        self.position = position   
        
        
    def setName(self,position):
        chars = ["A","B","C","D","E","F","G"]
        return chars[position[0]] + str(position[1])
    
      
    def set_occupied(self,player):
        '''set board position to occupied'''
        if self.occupied_by:
            raise Exception(f"Already occupied")

        self.occupied_by = player


    
class Tictactoe:
    def __init__(self,size = 3):
        self.size = size #currently only a size of 3 works
        self.gamedict = self.initialize_board()
        self.middle = (int((self.size-1)/2),int((self.size-1)/2)) if self.size % 2 else None  #not 0
        self.initialize_partition() #not sure if this is needed, tried to find some smarter way
       
        
    def initialize_board(self):
        position_dict = initialize_dict()
        game_dict = self.empty_board(self.size)
        i = 0
        for row in range(self.size):
            
            for col in range(self.size):
                bp = BoardPosition((row,col))
                game_dict[row][col] = bp
                position_dict[i] = bp
                i+=1
        self.position_dict = position_dict
        return game_dict
    

    
    def set_winner(self,winner):
        self.winner = winner
        
  
        
    def __str__(self):
        board = self.empty_board()
        gamedict = self.gamedict
        n = 1
        for i in range(3):
            for j in range(3):
                pos_obj = gamedict[i][j]
                board[i][j] = \
                   f'{n} ' if not pos_obj.occupied_by\
                     else self.player_to_char()[pos_obj.occupied_by]
                n +=1
        str_board = ""        
        for row in board.values():
            for value in row.values():
                str_board = f'{str_board} {value}'
            str_board = str_board + "\n"
        return str_board
        
    def player_to_char(self):
        return {1:"x ", 2:"o "}
    
    def occupy_spots(self,pos_player_dict):
        for pos,player in pos_player_dict.items():
            self.update_gamedict(pos,player)
            
    def update_gamedict(self,pos,player):
        self.gamedict[pos[0]][pos[1]].set_occupied(player)
        position = self.gamedict[pos[0]][pos[1]].position
        self.update_partition(pos,player)
       
    
    def flatten_board(self):
        flatten = {}
        
        for row in range(self.size):
            for col in range(self.size):
                flatten[(row,col)] = self.gamedict[row][col]
               
        return flatten
    
    def update_partition(self,pos,player):
        row,col = pos[0],pos[1]
        self.partition["rows"][row][col].set_occupied(player)
       
            

    def initialize_partition(self):
        rows = {i : [] for i in range(self.size)}
        columns = {i : [] for i in range(self.size)}
        diagonals = {i : [] for i in range(2)}
        
        for row in range(self.size):
            for col in range(self.size):
                bp = BoardPosition((row,col))
            
                rows[row].append(bp)
                columns[col].append(bp)
                
                if row == col:
                    diagonals[0].append(bp)
                if row + col == self.size-1:
                    diagonals[1].append(bp)
                    
        self.partition = {"rows" : rows, "columns" : columns, "diagonals" : diagonals}
     
    def get_partition_positions(self):
        rows = self.partition["rows"]
        for i in range(self.size):
            l = []
            for pos_obj in rows[i]:
                    l.append(pos_obj.position)
         
       # cols = self.partition["cols"]
       
       
    def print_partition(self):
        rows = self.partition["rows"]
        for i in range(self.size):
            l = []
            for pos_obj in rows[i]:
                    l.append(pos_obj.occupied_by)
            
            print(l)
        print("\n")
        cols = self.partition["columns"]
        for i in range(self.size):
            print([pos_obj.occupied_by for pos_obj in cols[i]])
        print("\n")
        diagonals = self.partition["diagonals"]    
        for i in range(2):
            print([pos_obj.occupied_by for pos_obj in diagonals[i]])
            
        
        
    def occupied_board(self):
       board = self.empty_board()
       for i in range(3):
           for j in range(3):
               board[i][j] = self.gamedict[i][j].occupied_by
               
       print(board)
       return board
        
    def is_empty(self,row,col):
        '''ckecks if the position on the board is empty. Returns True if Empty, False if not'''
        if self.gamedict[row][col].occupied_by: 
            return False
        return True
    
    def occupied_dict(self):
        occupied_dict = {i : {} for i in range(self.size)}
        for i in range(self.size):
            for j in range(self.size):
                occupied_dict[i][j] = self.gamedict[i][j].occupied_by
        return occupied_dict
                                   
    def check_win(self):
        """checks if someone has won (if every entry on a row, column or diagonal is equal)
        """
        occupied_dict = self.occupied_dict()
        
        size =  self.size
        for i in range(3):
            row_check = occupied_dict[i][0] == occupied_dict[i][1] == occupied_dict[i][2]
            if row_check and occupied_dict[i][0]:
                self.set_winner(occupied_dict[i][0])
                
        for j in range(3):
            column_check = occupied_dict[0][j] == occupied_dict[1][j] == occupied_dict[2][j]
            if column_check and occupied_dict[0][j]:
                self.set_winner(occupied_dict[0][j])
                
        diag1_check = occupied_dict[0][0] == occupied_dict[1][1] == occupied_dict[2][2]
        if diag1_check and occupied_dict[0][0]:
            self.set_winner( occupied_dict[0][0])
        
        diag2_check = occupied_dict[0][2] == occupied_dict[1][1] == occupied_dict[2][0]
        if diag2_check and occupied_dict[0][2]:
            self.set_winner(occupied_dict[0][2])
            
        return self.winner
    
   
    def empty_board(self,size=3):
        empty_board = {}
        for i in range(size):
            empty_board[i] = {j:None for j in range(size)}
        return empty_board
        

    def name_position(self):
        position_dict = {
      "A1":(0,0),
      "A2":(0,1),
      "A3":(0,2),
      "B1":(1,0),
      "B2":(1,1),
      "B3":(1,2),
      "C1":(2,0),
      "C2":(2,1),
      "C3":(2,2) } 
        return position_dict
    
    def position_name(self):
        return {pos:name for name, pos in self.name_position().items()}
    

board = Tictactoe()
#board.print_partition()
board.update_gamedict((1,1), 1)
board.update_gamedict((0,0), 2)
board.update_gamedict((0,1), 1)

print("\n")
print(board)
        



    
class Computer:
    
    def __init__(self,difficulty,num = 2):
        assert difficulty == 0 or difficulty == 0.5 or difficulty == 1 or difficulty == 2
        self.difficulty = difficulty
        self.num = num
        self.opponent = 1 if self.num == 2 else 2
        
    def set_difficulty(self,difficulty):
        self.difficulty = difficulty 
    
      
    def strategy0(self,game):
        '''make random move'''
        print("random")
        return self.random_move(game)
    
    def strategy0_5(self,game):
        '''random but favour middle'''
        middle = game.middle 
        midrow,midcol = middle[0],middle[1]
        if game.movesmade == 0: 
            return middle
        if not game.gamedict[midrow][midcol].occupied_by:
            return game.middle
        return self.random_move(game)
        
    def strategy1(self,game):
        '''check if we can block and if we can win'''
        if game.movesmade==1 or game.movesmade==0:
           # print("we skip calculate and do random")
            return self.random_move(game)
        
        move = self.move_calc(game)
        if move:
            return move
        return self.random_move(game)
        
    def strategy2(self,game):
        '''check for block and win and favour middle'''
        middle = game.middle 
        midrow,midcol = middle[0],middle[1]
        if game.movesmade == 0: 
            return middle
        move = self.move_calc(game) #check if we can win or if opponent can win
        if move:
            return move
        
        if game.is_empty(midrow,midcol):
            return middle
        return self.random_move(game)
    
    
    def random_move(self,game): 
        '''random move to empty position'''
        unoccupied_positions = []
        for row in range(game.size): 
            for col in range(game.size):
                if game.is_empty(row,col):
                    unoccupied_positions.append((row,col)) 
        if len(unoccupied_positions)==0:
            game.set_winner("draw")
            return None 
        
        random_pos = rand.choice(unoccupied_positions)
        return random_pos
    
   
    def check_pairs(self,game,player):
        #This has to be possible to do in some smarter/nicer way
      
        
        occupied_dict = game.occupied_dict()
        for i in range(3):
            if occupied_dict[i][0] == occupied_dict[i][1] == player and not occupied_dict[i][2]:
                return (i,2)
            elif occupied_dict[i][1] == occupied_dict[i][2] == player and not occupied_dict[i][0]:
                return (i,0)
            elif occupied_dict[i][0] == occupied_dict[i][2] == player and not occupied_dict[i][1]:
                return (i,1)                
                
        for j in range(3):
            if occupied_dict[0][j] == occupied_dict[1][j] == player and not occupied_dict[2][j]:
                return (2,j)
            elif occupied_dict[1][j] == occupied_dict[2][j] == player  and not occupied_dict[0][j]:
                return (0,j)
            elif occupied_dict[0][j] == occupied_dict[2][j] == player  and not occupied_dict[1][j]:
                return (1,j)
        
        if occupied_dict[0][0] == occupied_dict[1][1] == player  and not occupied_dict[2][2]:
            return (2,2)
        elif occupied_dict[1][1] == occupied_dict[2][2] == player  and not occupied_dict[0][0]:
            return (0,0)
        elif occupied_dict[0][0] == occupied_dict[2][2] == player  and not occupied_dict[1][1]:
            return (1,1)
        
        if occupied_dict[0][2] == occupied_dict[1][1] == player and not occupied_dict[2][0]:
            return (2,0)
        elif occupied_dict[1][1] == occupied_dict[2][0] == player and not occupied_dict[0][2]:
            return (0,2)
        elif occupied_dict[0][2] == occupied_dict[2][0] == player and not occupied_dict[1][1]:
            return (1,1)

        return None
        
    def move_calc(self,game): 
        gamedict = game.gamedict
        size =  game.size
        move = self.check_pairs(game, self.num) #first check if computer can win
        if move:
            return move
        move = self.check_pairs(game, self.opponent) #then check if other player can win
        if move:
            return move
    
        return None
       

        


        
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        


