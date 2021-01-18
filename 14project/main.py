from art import logo, vs
import random
from game_data import data

print(logo)

def game():
  play = 'y'
  while play == 'y':
    endgame = True
    scores = 0  
    firstacc = random.choice(data)
    first_name = firstacc["name"]
    first_desc = firstacc["description"]
    first_country = firstacc["country"]
    first_follow = firstacc["follower_count"]

    secondacc = random.choice(data)
    second_name = secondacc["name"]
    second_desc = secondacc["description"]
    second_country = secondacc["country"]
    second_follow = secondacc["follower_count"]
    while endgame:
      if scores >= 1:
        print(f"\nYou're right! current score: {scores}\n")
      print("_"*100)
      print(f"Compare A: {first_name}, a {first_desc}, from {first_country}: ")
      print(vs)
      print(f"Against B: {second_name}, a {second_desc}, from {second_country}: \n")
      print("_"*100)
      answer = input("Who has more subs? 'A' or 'B': ").upper()
      if first_follow > second_follow and answer == "A":
        scores += 1
        firstacc = random.choice(data)
        first_name = firstacc["name"]
        first_desc = firstacc["description"]
        first_country = firstacc["country"]
        first_follow = firstacc["follower_count"]
        secondacc = random.choice(data)
        second_name = secondacc["name"]
        second_desc = secondacc["description"]
        second_country = secondacc["country"]
        second_follow = secondacc["follower_count"]
      elif first_follow < second_follow and answer == "B":
        scores += 1
        firstacc = random.choice(data)
        first_name = firstacc["name"]
        first_desc = firstacc["description"]
        first_country = firstacc["country"]
        first_follow = firstacc["follower_count"]
        secondacc = random.choice(data)
        second_name = secondacc["name"]
        second_desc = secondacc["description"]
        second_country = secondacc["country"]
        second_follow = secondacc["follower_count"]
      else:
        print(f"Sorry that was wrong! You'r final score is {scores}")
        endgame = False
    
    play = input("Type 'y' to play agin: ").lower()
    
game()