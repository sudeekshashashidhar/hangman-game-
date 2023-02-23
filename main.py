import random

name = input("What is your name?: ")

print("That is a beautiful name. This is a hangman game. You get 15 guesses. Good Luck!")

words = ["encyclopedia", "mathematics", "basketball", "geography", "character", "congratulations"]

word = random.choice(words)

print("Guess the characters of the word.")

guesses = ""

turns = 15

while turns > 0:
  failed = 0
  for char in word:
    if char in guesses:
      print("Correct!")
      print(char)
      

    else:
      print("_")

      failed += 1

  if failed == 0:
    print("Congratulations!! You win!")
    print("The word is: ", word)
    break

  guess = input("Guess a character(lower case only!):")

  guesses += guess

  if guess not in word:
    turns -= 1

  print("Wrong! Guess again.") 

  print("You have", + turns, "more guesses.")

  if turns == 0:
    print("You loose, better luck next time!")
      