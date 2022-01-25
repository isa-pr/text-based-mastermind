import os
def highscore(difficulty, score):
  '''
  From parameters difficulty and score, creates a text file that stores the difficulty, score, and name of player.
  '''
  def scoreBoard(path, difficulty, score):
      score = str(score)
      difficulty = str(difficulty)

      board = []
      with open(path, "r") as fileRead:
          reader = fileRead.readlines()
          for i in reader:
              scores = i.split()
              board.append(scores)

      for j in range(len(board)):
          if difficulty == board[j][0]:
              if board[j][2] == "-" or int(score) < int(board[j][2]):
                  print(f"Congratulations! You got the highest score for Level {difficulty}.")
                  name = getName()
                  board[j][1] = name
                  board[j][2] = score
                  break

              elif int(score) == int(board[j][2]) == 1:
                print(f"Congratulations! But {board[j][1]} already got the highest score.")
              
              elif int(score) >= int(board[j][2]):
                if int(score) == int(board[j][2]):
                  print(f"Good Try! But {board[j][1]} already got the same score. Try harder.")
                
                elif int(score) > int(board[j][2]):
                  print(f"Good Try! But {board[j][1]} got a higher score. Try again.")

              break

      newBoard = ""
      print("\n\tScoreboard\n")
      print("Level\tScore\tName")
      for k in board:
          winners = f"{k[0]}    \t{k[2]}\t{k[1]}"
          print(winners)
          newBoard = newBoard + f"{k[0]}\t{k[1]}\t{k[2]}" + "\n"

      with open(path, "w") as fileWrite:
          fileWrite.write(newBoard)

  def getName():
      while True:
          name = input("Enter your Name: ").strip().upper()
          if (len(name) < 8 and len(name) > 0) and " " not in name:
              return name 
          
          print("Invalid! Can only take 1-7 characters and no spaces.\n")

  fileName = "scoreboard.txt"
  fileExists = os.path.isfile(f"./{fileName}")

  if not fileExists:
      with open(fileName, 'w') as f:
          text = f"4 - -\n5 - -\n6 - -\n7 - -\n8 - -" # Starting line
          f.write(text)
          print(f"File not found. Making new file.\n")

  scoreBoard(fileName, difficulty, score)