'''
Conanan, Lanz Anjelo L. - 2021-02338 - T4
Felipe, Joshua L. - 2021-11579 - T4
Padua, Maria Isabel - 2013-14838 - T4
'''

"""
NEVER FORGET: Zip file Naming scheme - `CS11MP1_T4_Conanan_Felipe_Padua`

Legends:
[ ] - Not Started
[P] - In progress
[R] - For Review
[T] - For Testing/Debugging
[/] - Done

Program Checklist:            Last modified Date
[/] Main Script               01/10/22
[/] CodeSequenceGeneration    12/29/21
[/] GameInput                 01/09/22
[/] CheckGuess                01/09/22
[/] LifelineRequest           01/09/22

Additional Features:
[/] Level of Difficulty       12/29/21
[/] Reset & Quit within Game  01/09/22
[/] High Score                01/09/22

Documentation:
[/] User Manual               01/09/22
[/] Implementation            01/10/22
[/] References                01/09/22

"""

from feedback import CheckGuess
from codeGenerator import SequenceGenerator
from inputs import GameInput
from score import highscore
from os import system

if __name__ == "__main__":
  playingGame = True

  while playingGame:
    
    playingRound = True
    
    masterSeq = SequenceGenerator()
    print(f"Hidden code is of length {len(masterSeq)}.\n"
    f"Total number of Guesses: 10\n")

    attempts = 10
    markedAnswer = masterSeq[:]
    lineUsed = False

    print(markedAnswer)

    while attempts > 0 and playingRound:
      answer = masterSeq[:]

      KeepPlaying, attempts, guess, markedAnswer, lineUsed = GameInput(attempts, answer, markedAnswer, lineUsed)

      KeepPlaying, markedAnswer = CheckGuess(guess, answer, markedAnswer)

      if KeepPlaying == "continue":
        continue

      elif KeepPlaying == "win":
        print("You Win!\n")
        score = 10 - attempts
        difficulty = len(answer)
        highscore(difficulty, score)
        playingRound = False

      elif KeepPlaying == "reset" or KeepPlaying == "quit":
        playingRound = False

    if attempts == 0 or playingRound == False: #End state
      if attempts == 0 and KeepPlaying != "win":
        print("You Lost!\nCorrect sequence: " + "".join(masterSeq))
      print()
      
      while True:
        resetQuery = str(input("Type 'reset' to play again or 'quit' to exit: ")).strip().lower()
        
        if resetQuery == "reset":
          print("Resetting game\n")
          playingRound = False
          break
        
        elif resetQuery == "quit":
          print("Thanks for playing!\n")
          playingRound = False
          playingGame = False
          break
        
        else:
          print("Invalid Input.\n")

  system("pause")