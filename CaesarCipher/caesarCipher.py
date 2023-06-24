alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    msg = []
    for i in text:
        msg.append(i)
    for i in range(len(msg)):
        index = alphabet.index(msg[i])
        shifted_index = (index + shift) % len(alphabet)
        msg[i] = alphabet[shifted_index]
    print("".join(msg))

def decode(text, shift):
    msg = []
    for i in text:
        msg.append(i)
    for i in range(len(msg)):
        index = alphabet.index(msg[i])
        shifted_index = (index - shift) % len(alphabet)
        msg[i] = alphabet[shifted_index]
    print("".join(msg))



if direction == "encode":
    encrypt(text = text, shift = shift)
elif direction == "decode":
    decode(text = text, shift = shift)