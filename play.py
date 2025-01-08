## Rock Paper Scissor Game

## This is a game in which user and computer which choose one option from rock, paper and scissor.
## Game follow a given rull 

## ROCK VS PAPER => PAPER will be win so user with PAPER selection will be win.
## PAPER VS SCISSOR => SCISSOR will be win so user with SCISSOR selection will be win.
## SCISSOR VS ROCK = > ROCK will be win so user with ROCK selection will be win

##  Author Details 

## Name  :  Er. Amar kumar 
## Email :  amarkumar9685079691@gmail.com 

## Start of a Game ##

import random


class RockPaperScissorGame: 

    _choices = {
        1 : "ROCK",
        2 : "PAPER",
        3 : "SCISSOR" 
    }

    _user_choice = 0
    _computer_choice = 0

    def _welcomeMessage(self):  
        print("\n*Note: GAME will follow given rules to select winner\n")
        print("1. ROCK VS PAPER => PAPER will be win so user with PAPER selection will be selected as winner ")
        print("2. PAPER VS SCISSOR => SCISSOR will be win so user with PAPER selection will be selected as winner ")
        print("3. SCISSOR VS ROCK = > ROCK will be win so user with PAPER selection will be selected as winner ")
    

    def _resetGameState(self):
        self._user_choice = 0
        self._computer_choice = 0
    
    def _GameOverState(self, winner):
        if winner == "Computer":
           print("\n\nYou lost the game")
        else : 
            print("\n\nConfiguration!")
            print("You won the game!")
        
        StartHandler()


    def _selectionMessage(self):
        for key, value in self._choices.items():
            print(f"\nSelect {key} for select a {value} as your choice")
    
    def _userTurn(self):
        print("\nYour turn..")
        self._selectionMessage()
        self._user_choice = int(input("\nEnter your choice: "))
        
        while self._user_choice not in self._choices.keys():
            print("Please choose valid option! ")
            self._user_choice = int(input("Enter your choice: "))


    def _findWinner(self):
    
        if self._user_choice  == self._computer_choice:
            print("Oh! GAME TIE")  
        elif (self._user_choice == 1 and self._computer_choice == 2) or (self._user_choice == 3 and self._computer_choice == 1) or (self._user_choice == 2 and self._computer_choice == 3):
            self._GameOverState("Computer") 
        elif (self._user_choice == 2 and self._computer_choice == 1) or (self._user_choice == 1 and self._computer_choice == 3) or (self._user_choice == 3 and self._computer_choice == 2):
            self._GameOverState("User")
    

    def play(self):
        try:
            self._welcomeMessage()
            print("\nDo you want to start first or second?")
            start_choice = str(input("Type F for first  and S for second turn "))

            if start_choice == 'F':
                self._userTurn()
                print("\nComputer turn")
                self._computer_choice = random.randint(1,3)
                print(f"\nComputer selected {self._choices[self._computer_choice]}")
            else: 
                print("\nComputer turn")
                self._computer_choice = random.randint(1,3)
                print(f"\nComputer selected {self._choices[self._computer_choice]}")
                self._userTurn()
            
            self._findWinner()
        
        except KeyboardInterrupt:
            print("Okay Bye, See you again!")
            exit(0)


       

# helper function to play game 

def StartHandler():
    print("Do you want to play game?")
    should_play = int(input("Type 1 for yes or 2 for exit "))

    if should_play == 1:
       print("Best of luck!")
       game = RockPaperScissorGame()
       game.play()
    else: 
       print("Bye! see you again!")
       exit(0)

## End of Game


if __name__ == "__main__":
    print("Welcome at ROCK - PAPER - SCISSOR GAME! ") 
    StartHandler()