# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:05:08 2024

@author: olivi
"""

from Tictactoe import *


class Simulation(Tictactoe):
    
    def __init__(self,startplayer, difficulty1, difficulty2):
       super().__init__()
       self.size = 3
       self.startplayer = startplayer

       self.computer1 = Computer(difficulty1,1)
       self.computer2 = Computer(difficulty2,2)
       self.prevturn = None
       self.movesmade = 0
       self.winner = None
       
     
    def move_computer(self,computer):

        if computer.difficulty == 0:
            move = computer.strategy0(self)
        elif computer.difficulty == 1:
            move = computer.strategy1(self)
        elif computer.difficulty == 0.5:
            move = computer.strategy0_5(self)
        elif computer.difficulty == 2: 
            move = computer.strategy2(self)
            
        if not move and not self.winner:
            raise Exception("Something went wrong")
        
        if move:
            self.update_gamedict(move,computer.num)
            self.prevturn = computer.num
            self.movesmade = self.movesmade +1
            
        
    def simulate_match(self,print_board = False):
        startplayer = self.computer1 if self.startplayer==1 else self.computer2
        assert startplayer.num == self.startplayer
      #  print(self.startplayer)
       # print(self.computer1.num,self.computer1.difficulty)
       # print(self.computer2.num,self.computer2.difficulty)
        while True:
            
            if self.winner:
                if self.winner == "draw":
                    if print_board:
                        print("it's a draw!") 
                    return "draw"
                if print_board:
                    print(f'{self.winner} won!')
                return self.winner
                
            if self.movesmade == 0:
                self.move_computer(startplayer)
            
                
            else:
                if self.prevturn == 1:
                    self.move_computer(self.computer2)
                elif self.prevturn == 2:
                    self.move_computer(self.computer1)
                self.check_win()
            if print_board:
                print(self)
            #print(f'moves: {self.movesmade}')
           # print(f'player: {self.prevturn}')




    
def random_startplayer():
    ''' 
    return 1 (player) or 2 (computer)
    '''
    randomint = rand.randint(1,2)
    return randomint


print(random_startplayer())
sim = Simulation(random_startplayer(), 1,1)
print(sim.startplayer,sim.simulate_match())


def simulate_n_matches(startplayer,dif1,dif2,n=1000):
    
    comp1 = 0 
    comp2 = 0
    draw =0
    countplayer = 0
    startp = startplayer
    for i in range(n):
        
        if startplayer == "random":
            startp= random_startplayer()
        if startp ==1:
            countplayer +=1
         
        sim = Simulation(startplayer = startp,difficulty1=dif1,difficulty2=dif2)
        result = sim.simulate_match(print_board = False)
        if result == 1:
            
            comp1 += 1
        elif result == 2:
            comp2 += 1
        elif result =="draw":
            draw +=1
            
    print(f'player 1 win: {comp1} \nplayer 2 win: {comp2} \ndraw: {draw}')
    print(countplayer)
    print_results(comp1,comp2,draw)
    
    
def print_results(wins_player1,wins_player2,draws):
    results = [wins_player1,wins_player2,draws]
    names = ["robot 1","robot 2","draw"]
    plt.bar(names,results)
    plt.ylabel('fruit supply')
    plt.title('Fruit supply by kind and color')
    plt.show()
  

simulate_n_matches(startplayer ="random",dif1 =1,dif2=2,n=1000)
