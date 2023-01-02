from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift, direction):
  chipher_text=""
  if direction=="decode":
    shift *= -1
  for i in plain_text:
    if i not in alphabet:
      chipher_text += i
    else:
      position=alphabet.index(i)
      new_position=position+shift
      new_position=new_position%26
      new_letter=alphabet[new_position]
      chipher_text += new_letter
  print(chipher_text)
yesno_check=False
restart_check=True
while restart_check==True and yesno_check==False:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if direction=="encode" or direction=="decode":
    caesar(plain_text=text,shift=shift,direction=direction)
    yesno_check=True
    while yesno_check==True and restart_check==True:        
      ask_restart=input("Do you want to restart program: Yes/No").lower()
      if ask_restart=="no":
        restart_check=False
        yesno_check=False
      elif ask_restart=="yes":
        restart_check=True
        yesno_check=False
  else:
    print("Please type right command")
