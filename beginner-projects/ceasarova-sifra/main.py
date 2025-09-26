alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

message = input("Type your massage : ")
# shift_number = input("Type the shift number : ")
# funkciu na zakodovanie a decodovanie správy

massage1= []

def code ():
    

for x in message:
    massage1.append(x)
    for znak in massage1:
        if znak.isalpha():
            codding(x)
print(massage1)
# def encode(message , shift_number):
    