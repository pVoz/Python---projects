alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c',
            'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message,shift_number):
            shifted_text = ""
            for one_letter in message:
                if one_letter != " ":
                    index = alphabet.index(one_letter)
                    new_index = index + int(shift_number)
                    shifted_text += alphabet[new_index] 
                else : 
                    shifted_text += one_letter
            print (f"Your encrypted text is : {shifted_text}")
            # return shifted_text
# encrypted_message = encode(message,shift_number)  
def decode(encrypted_message, shift_number):
        normal_text = ""
        for one_letter in encrypted_message:
            if one_letter != " ":
                index = alphabet.index(one_letter)
                new_index = index - int(shift_number)
                normal_text += alphabet[new_index]
            else:
                normal_text += one_letter
        print (f"Your decrypted text is : {normal_text}")  
def msg():
    message = input("Type your massage : ").lower()
    shift_number = input("type your number :")
    return message ,shift_number
# msg(message,shift_number)

def uloz(text):
     with open("heslo.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")
        
while True:
    job = input(f"write 'encode' or 'decode' : ")
    
    if job == "decode":
        message, shift_number = msg()
        # msg(message,shift_number)
        decode(message,shift_number)
        # uloz(shifted_textt)
    elif job == "encode":
        message, shift_number = msg()
        # message = input("Type your massage : ").lower()
        # shift_number = input("type your number :")
        encode(message,shift_number)
    else :
        print("You need to choice right word!")
    
   
