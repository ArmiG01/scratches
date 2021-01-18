print(" Welcome to Tresure island.\n Your mission is to find the tresure.\n")
choise = str(input("Ты можешь пойти 'налево' или 'направо'?  что выберешь? ")).lower()
if choise == "направо" or choise == "налево":
  if choise == "направо":
    print("GAME OVER")
  elif choise == "налево":
    choise = str(input("Ты видишь корабль в море, что выберешь, подплыть или ждать? ")).lower()
    if choise == "подплыть" or choise == "ждать":
      if choise == "подплыть":
        print("GAME OVER")
      elif choise == "ждать":
        choise = str(input("Ты на корабле, перед тобой жёлтая дверь, ты можешь спуститься на палубу, покинуть корабль или зайти в дверь? ")).lower()
        if choise == "спуститься на палубу" or choise == "покинуть корабль" or choise == "зайти в дверь":
          if choise == "зайти в дверь":
            print("WIN")
        else:
          print("Действие недоступно, выберите одну из предложенных!")
    else:
      print("Действие недоступно, выберите одну из предложенных!")       
else:
  print("Действие недоступно, выберите одну из предложенных!")