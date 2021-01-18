from art import logo
print(logo)
def calculator():
  def add(n1, n2):
    return  n1 + n2
  def sub(n1, n2):
    return  n1 - n2
  def multiply(n1, n2):
    return  n1 * n2
  def divide(n1, n2):
    return  n1 / n2

  operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
  }
  num1 = float(input("What's first num? "))
  for i in operations:
    print(i)
  selected = input("Choose an operator ")
  num2 = float(input("What's second num? "))
  calc = operations[selected]
  answer = calc(num1, num2)
  print(f"{num1} {selected} {num2} = {answer}")

  done = True
  while done:
    if input("press 'y' for continue, press 'n' for starting again ") == "y":
      new_oper = input("Pick another operation: ")
      num3 = float(input("print next number "))
      calc = operations[new_oper]
      someanswer = answer
      answer = calc(answer, num3)
      print(f"{someanswer} {new_oper} {num3} = {answer}")
    else:
      print(f"last answer was {answer}")
      done = False
      calculator()
calculator()