def CheckGuess(guessList, answerList, markedAnswer):
  '''
  Parameters guess, unmarked, answer, & marked Answer are used to check if the guess is correct (or if the user wants to reset or quit). Otherwise, it prints out feedback on the guess.
  Returns Game State determiner and markedAnswer
  '''

  if "".join(guessList) == "".join(answerList):
    return "win", markedAnswer

  elif guessList == "reset":
    return "reset", markedAnswer
    
  elif guessList == "quit":
    return "quit", markedAnswer

  r = 0
  w = 0

  guess = guessList[:]
  answer = answerList[:]

  # Marks all the correct Rs
  for j in range(len(guess)):
    if guess[j] == answer[j]:
      r += 1
      answer[j] = guess[j] = markedAnswer[j] = "R"

  # Marks all the correct Ws
  for i in guess:
    if i in answer and i != "R":
      w += 1
      index = answer.index(i)
      answer[index] = "W"
      if markedAnswer[index] != "W":
        markedAnswer[index] = "W"
  
  print(f"{r}R - {w}W\n")

  return "continue", markedAnswer