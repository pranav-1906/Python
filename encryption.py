import random
import string
import time

chars = string.digits + string.ascii_letters + string.punctuation + " "
chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

#encrypt
text = input("Enter your text:")
encrypted = ""

for letter in text:
    index = chars.index(letter)
    encrypted += keys[index]

print(f"Encrypted text: {encrypted}")

time.sleep(1)

#decrypt
encrypted = input("Enter encrypted text:")
decrypted = ""

for letter in encrypted:
    index = keys.index(letter)
    decrypted += chars[index]

print(f"Decrypted text: {decrypted}")