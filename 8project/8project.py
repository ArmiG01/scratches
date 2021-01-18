from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
repeat = True
def caesar(text =text, shift = shift, direction = direction):
  text_to_list = list(text)
  encody = []
  decody = []
  if direction == "encode":
    for letter in range(len(text_to_list)):
      if text_to_list[letter] in alphabet:
        if alphabet.index(text_to_list[letter]) + shift <= len(alphabet)-1:
          encody += alphabet[alphabet.index(text_to_list[letter]) + shift]
        else:
          undo = alphabet.index(text_to_list[letter]) + shift
          while undo > len(alphabet)-1:
            undo -= len(alphabet)
          encody += alphabet[undo]
      else:
        encody += text_to_list[letter]
    listToString = ''.join(map(str, encody))
    print(f"encoded text is {listToString}")
  elif direction == "decode":
    for letter in range(len(text_to_list)):
      if text_to_list[letter] in alphabet:
        if alphabet.index(text_to_list[letter]) - shift >= 0:
          decody += alphabet[alphabet.index(text_to_list[letter]) - shift]
        else:
          undo = alphabet.index(text_to_list[letter]) - shift
          while undo < 0:
            undo += len(alphabet)
          decody += alphabet[undo]
      else:
        decody += text_to_list[letter]
    listToString2 = ''.join(map(str, decody))
    print(f"decoded text is {listToString2}")
  

caesar()
while repeat:
  repeating = input(f" Print 'Yes' for use {direction} again again\n print 'Change' for changing direction\n print 'No' for exit ").lower()
  if repeating == "yes":
    new_text = input("Type your message:\n").lower()
    new_shift = int(input("Type the shift number:\n"))
    caesar(text = new_text, shift = new_shift)
  elif repeating == "change":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    new_text = input("Type your message:\n").lower()
    new_shift = int(input("Type the shift number:\n"))
    caesar(text = new_text, shift = new_shift, direction = direction)

  else:
    repeat = False


    
