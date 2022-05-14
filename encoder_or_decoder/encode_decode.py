
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'
, 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'
, 'x', 'y', 'z']
from unittest import result
from art import logo
print(logo)

    





def  cipher(cipher_text,shift_amount,direction_choice):
    
    
    if direction_choice=="encode":
        encode_text=""
        for letter in cipher_text:
            position = alphabet.index(letter)
            
            new_position= position + shift_amount
            new_letter = alphabet[new_position]
            encode_text+=  new_letter
            

        print(f"the encoded text is {encode_text}")
    elif direction_choice=="decode":
        decode_text=""
        for letter in cipher_text:
                position = alphabet.index(letter)
                new_position= position - shift_amount
                new_letter = alphabet[new_position]
                decode_text+=  new_letter
        print(f"the decoded text is {decode_text}")
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    cipher(cipher_text=text,shift_amount=shift,direction_choice=direction)
    result=input("Type yes if you want to continue,type No to stop\n")
    if result=="no":
        should_continue=False
        print("Bye")









    
    


    
    
