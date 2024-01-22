# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:35:17 2024

@author: olivi
"""

import unittest
from Tictactoe import Tictactoe
from Tictactoe import Computer
from Game import Game



def print_board(game):
    board = game.empty_board()
    for i in range(3):
        for j in range(3):
            board[i][j] = game.gamedict[i][j].occupied_by
            
    print(board)
    return board
    
class test_main(unittest.TestCase):
    
    def test_board(self):
        board = Tictactoe()
       # for i in range(3):
           # for j in range(3):
              ##  print(board.gamedict[i][j].position, board.gamedict[i][j].name)
                
        self.assertEqual(board.middle, (1,1))
        self.assertEqual(Tictactoe(size=5).middle,(2,2)) 
        self.assertEqual(Tictactoe(size=6).middle,None)
        
    def test_occupied_by(self):
        game = Game()
        with self.assertRaises(Exception):
            game.gamedict[0][0].set_occupied_by(2)
            game.gamedict[0][0].set_occupied_by(1)
             
    
    def test_Computer(self):
        
        game = Game(difficulty = 0)
        print_board(game)
        game.move_computer()
        self.assertEqual(game.movesmade,1)
        self.assertEqual(game.prevturn,2)
    
        
        game = Game()
        print_board(game)
        game.move_computer()
        self.assertEqual(game.movesmade,1)
        self.assertEqual(game.prevturn,2)
        print(game.prevturn)
        print_board(game)
        print(game)
        
        game = Game(difficulty=2)
        game.move_computer()
        self.assertEqual(game.movesmade,1)
        self.assertEqual(game.prevturn,2)
        self.assertEqual(game.gamedict[1][1].occupied_by, 2)
        print_board(game)
        print(game)
        
        game = Game(difficulty=2)
        game.gamedict[0][0].set_occupied(2)
        game.gamedict[0][1].set_occupied(1)
        game.gamedict[0][2].set_occupied(2)
        game.gamedict[1][0].set_occupied(1)
        
        board = Tictactoe()
        board.occupy_spots({(0,0):2,(0,1):1,(0,2):2,(1,0):1,(1,1):2})
        print(board)
        self.assertEqual(game.computer.strategy2(game),(1,1))
        print(game)
        
        


unittest.main()




c1 = Computer(0)
c2 = Computer(1)
c3 = Computer(2)
