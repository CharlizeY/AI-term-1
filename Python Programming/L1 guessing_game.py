secretNumber = 50
userGuess = input("Please enter a number from 1 to 100: ")
userGuess = int(userGuess)
maxGuesses = 3
numofGuesses = 1

while userGuess != secretNumber and numofGuesses < maxGuesses:
      print("incorrect")
      if abs(userGuess - secretNumber) < 10:
         print("cold")
      else:
         print("hot")
      userGuess = input("Please enter a number from 1 to 100: ")
      userGuess = int(userGuess)
      numofGuesses = numofGuesses + 1
      
if userGuess == secretNumber:
    print("correct")
else:
    print("incorrect")
    if abs(userGuess - secretNumber) < 10:
         print("cold")
    else:
         print("hot")
    print("Game is over.")





