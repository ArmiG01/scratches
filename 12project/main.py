from random import randint
from art import logo
print(logo)
print("Welcome to the Number Guessing Game! ")
EASY = 10
HARD = 5
answer = randint(1,100)
print("I'm thinking of a number between 1 and 100 ")
dificulty = input("Choose a difficulty. Type 'easy' or 'hard' ")
def game():
  if dificulty == 'hard':
    lives = HARD
    gamend = True
    print(f"You have {lives} attempts remaining to guess the number. ")
    guess = int(input("Make a Guess: "))
    while gamend:
      if lives != 0:
        if guess > answer:
          print("Too high ")
          print("Guess again: ")
          lives -= 1
          print(f"You have {lives} attempts remaining to guess the number. ")
        elif guess < answer:
          print("Too low ")
          print("Guess again: ")
          lives -= 1
          print(f"You have {lives} attempts remaining to guess the number. ")
        elif guess == answer:
          print("You Win 🤩")
          gamend = False
      if guess != answer:
        guess = int(input("Guess again: ")) 
      if lives == 1:
        print("You've run out of guesses, you lose. 🥶")
        gamend = False
  else:
    lives = EASY
    gamend = True
    print(f"You have {lives} attempts remaining to guess the number. ")
    guess = int(input("Make a Guess: "))
    while gamend:
      if lives != 0:
        if guess > answer:
          print("Too high ")
          print("Guess again: ")
          lives -= 1
          print(f"You have {lives} attempts remaining to guess the number. ")
        elif guess < answer:
          print("Too low ")
          print("Guess again: ")
          lives -= 1
          print(f"You have {lives} attempts remaining to guess the number. ")
        elif guess == answer:
          print("You Win 🤩")
          gamend = False
      if guess != answer:
        guess = int(input("Guess again: "))
      if lives == 1:
        print("You've run out of guesses, you lose. 🥶")
        gamend = False

game()
