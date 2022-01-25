from random import randint
def SequenceGenerator():
  '''
  Asks user for desired difficulty level and returns a randomly generated list of string values (0-9)
  '''
  invalidInput = True

  while invalidInput:
    level = input("\nEnter difficulty level [4-8 or random]> ").strip().lower()

    if level == "random":
      level = randint(4,8)
      masterSeq = [str(randint(0,9)) for i in range(level)]
      invalidInput = False
    
    elif level.isnumeric() and (4 <= int(level) <= 8):
      masterSeq = [str(randint(0,9)) for i in range(int(level))]
      invalidInput = False

    else:
      print("Invalid Input. Input should be from 4 to 8 (inclusive) or 'random'.")
  
  return masterSeq 