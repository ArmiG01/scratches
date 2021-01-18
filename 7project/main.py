import random
from art import logo, stages
from words import word_list
chosen_word = random.choice(word_list).upper()

display = []
for letter in chosen_word:
  display += "_"
length = len(chosen_word)
end = False
lives = 6
false = []
entered = []
print(logo)
while not end:
  while "_" in display and lives > 0:
    if not end:
      print(stages[lives])
    guess = str(input("Guess a letter! ")).upper()
    if len(guess) == 1:
      for position in range(length):
        if guess == chosen_word[position]:
          display[position] = chosen_word[position]
      if guess in entered:
        print(f"Choose another word, {guess} is already chosen")
      elif guess not in entered:
        entered += guess
        if guess not in display:
          lives -=1
      print(display)
      print(f"Your typing history {entered}")

      if lives == 0:
        print(stages[lives])
        print("You lose")
        end = True
      if not "_" in display:
        end = True
        print("You win")
    else:
      print("You lose! We need char (char is a 1 letter, not more, not less)! ")






