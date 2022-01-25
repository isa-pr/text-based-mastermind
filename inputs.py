"""
Temp notes:
To determine what error it has, else block would check if guess is all digits and if it is in the same as length answer.
Second conditional checks if the input has alphanumeric characters that would result to ValueError.
Lastly, an else block would catch any unexpected inputs that would result to an error, such as blank inputs, other characters etc.  If an error arises from the inputs it would loop back to asking a guess until a valid guess would be given.

GameInput Funtion specification:

"""
import random

def LifelineRequest(kind, attempts, answer, markedAnswer, lineUsed):
  '''
  Takes kind of lifeline, attempts remaining, master sequence, marked Answer, and lineUsed. Outputs requested lifeline and returns attempts remaining, new marked answer, and lineUsed
  '''
  if lineUsed:
    print("Cannot call lifeline as you've already used one before\n")

  elif kind == "lifeline#1" and attempts > 1:
    choices = [i for i in markedAnswer if i != "R" if i != "W"] #Filters out marked pegs

    if not choices:
      print("You already know all the numbers. Redundant lifeline.\n")
    
    else:
      choice = random.choice(choices)
      lineUsed = True
      attempts -= 1
      print(f"Number {choice} is in the sequence.\nNote: Total number of guesses is reduced by 1.\n")
      markedAnswer[markedAnswer.index(choice)] = "W"

  elif kind == "lifeline#2" and attempts > 2:
    #Create a list of pegs' index to preserve their position values
    positions = [i for i in range(len(markedAnswer)) if (markedAnswer[i] != "R")]

    if not positions:
        print("You already know all the numbers and their positions. Redundant lifeline. Go win the game.\n")
    
    else:
      position = positions[random.randint(0, len(positions)-1)]
      choice = answer[position] #Use randomly picked position to access value from master sequence
      lineUsed = True
      attempts -= 2
      print(f"Number {choice} is found at position {position + 1}\nNote: Total number of guesses is reduced by 2.\n")
      markedAnswer[position] = "R"
    
  else:
      print(f"Invalid Input.\nCannot call lifeline as you only have {attempts} guesses left\n")

  return attempts, markedAnswer, lineUsed

def GameInput(attempts, answer, markedAnswer, lineUsed):
  '''
  Parameters are attempts remaining, master answer sequence, marked answer list, and lineUsed.
  Function continuously takes user input, validates it, and processes it appropriately.
  Returns these values.
  - Game state determiner (e.g., quit, continue, etc.)
  - Attempts remaining after attempts are used
  - The user's guess
  - marked answer
  - lineUsed
  '''

  while True:
    print(f"Guess #{11 - attempts} of 10:")
    guess = input("Enter guess> ").strip().lower()
    
    if guess == "lifeline#1" or guess == "lifeline#2":
      attempts, markedAnswer, lineUsed = LifelineRequest(guess, attempts, answer, markedAnswer, lineUsed)

    elif guess == "quit":
      return "quit", attempts, guess, markedAnswer, lineUsed

    elif guess == "reset":
      return "reset", attempts, guess, markedAnswer, lineUsed

    elif len(guess) == len(answer) and guess.isnumeric():			
      attempts -= 1
      return "continue", attempts, list(guess), markedAnswer, lineUsed

    else:
      if len(guess) != len(answer) and guess.isnumeric():
        print(f"Invalid guess.\nGuess should be of length {len(answer)}.\n")

      elif guess.isalnum():
        print(f"Invalid guess.\nGuess only takes integers, 'lifeline#1', 'lifeline#2', 'reset', or 'quit'.\n")

      else:
        print(f"Invalid guess.\nGuess contains invalid characters.\n")