from art import logo
print(logo)
print("Welcome to the secret auction program")
name = input("What is your name?: ")
money = int(input("What's your bid?: "))
allplayers = {}
def auction(nameadd = name, bid = money):
  allplayers[nameadd] = bid
auction()
end = False

while not end:
  others = input("(Yes, No) Is there anybody who want to bid?: ").lower()
  if others == "yes":
    name = input("What is your name?: ")
    money = int(input("What's your bid?: "))
    auction(nameadd = name, bid = money)
    max_bid = []
    for i in allplayers:
      max_bid.append(allplayers[i])
  else:
    maximum = max(max_bid)
    maxindex = max_bid.index(maximum)
    keys = list(allplayers.keys())
    print(f"This auction is going to {keys[maxindex]} by bidding ${maximum}")

    end = True







