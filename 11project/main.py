import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
endgame = False
def deal_card():
  return random.choice(cards)




for i in range(2):
  computer.append(deal_card())
  if deal_card() == 11:
    if sum(user) + 11 < 21:
      user.append(11)
    else:
      user.append(1)
  else:
    user.append(deal_card())

def calculation(cards):
  if sum(cards) == 21:
    return 0
  elif sum(cards) == 21:
    return 0
  else:
    return sum(cards)

def result():
  if calculation(user) == 0:
    return "   You got luccky, blackjack\n   You WIN!😄 "
  elif calculation(computer) == 0:
    return "   Computer got luccky, blackjack\n   You LOSE!😱 "
  elif calculation(user) > 21:
    return "   You're out of range...\n   You LOSE!😱 "
  elif calculation(computer) > 21:
    return "   computer's out of range...\n   You WIN!😄 "
  elif calculation(user) > calculation(computer):
    return "   You WIN!😄 "
  else:
    return "   You LOSE!😱 "
print(logo)
print(f" User's cards {user} and sum is {calculation(user)}\n")
print(f" Computer's first cards {computer[0]}\n")
if calculation(user) < 21 and calculation(user) != 0:
  while not endgame:
    if calculation(user) < 21:
      choice = input("   Press 'y' to get another card and 'n' for passing ")
      if choice == 'y':
        if deal_card() == 11:
          if sum(user) + 11 < 21:
            user.append(11)
          else:
            user.append(1)
        else:
          user.append(deal_card())
        print(f" User's cards {user} and sum is {calculation(user)}\n")
        print(f" Computer's first cards {computer[0]}\n")
      else:
        endgame = True
    else:
      endgame = True
else:
  endgame = True
if calculation(user) != 0 and calculation(user) < 21:
  endgame2 = False
  while not endgame2:
    if calculation(computer) < 17 and calculation(computer) != 0:
      computer.append(deal_card())
      if calculation(computer) > 21:
        endgame2 = True
    else:
      endgame2 = True
  print(f" User's cards {user} and sum is {calculation(user)}\n")
  print(f" Computer's set is {computer}\n")
print(result())  



