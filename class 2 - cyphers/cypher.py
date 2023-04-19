# we will implement a cyclical cypher in this code as a way to learn Python.
# the idea is that each letter of the alphabet is shifted by a fixed amount. So if a is 0, b is 1 etc...
# and we shift by x = 1, then each 'a' will be a 'b', each 'b' a 'c' etc...

# we will only use functions (no classes) in this tutorial.
# at this point I haven't yet introduced classes so it's beyond the scope of this tutorial even though it
# would make the code a lot cleaner.

# steps:

# 1. create a mapping between letters for the alphabet based on a fixed offset.
# 2. use the mapping to encrypt a message (string).
# 3. use the mapping in reverse to decrypt it.

## 1. Map the alphabet

#global variables
alphabet = "abcdefghijklmnopqrstuvwxyz"

def create_cypher_map_1(offset):
    i = 0
    mapping = {}
    reverse_mapping = {}
    for letter in alphabet:
        index = i + offset
        if index > len(alphabet) - 1: # counting starts at 0, so we need the -1
            index = index - len(alphabet) # we start over when we are outside of the range
        mapping[letter] = alphabet[index]
        reverse_mapping[alphabet[index]] = letter
        i += 1 # increment
    return mapping, reverse_mapping

straight_map, reverse_map = create_cypher_map_1(1)

print(straight_map)
print(reverse_map)

def encrypt_decrypt(text : str, map):
    result = ""
    for letter in text:
        if letter.isupper():
            # then we need to lower it
            a = letter.lower()
            b = map[a].upper()
        else:
            b = map[letter]
        result += b
    return result

cypher_text = encrypt_decrypt("Enrique", straight_map)
print(cypher_text)

decyphered_text = encrypt_decrypt(cypher_text, reverse_map)
print(decyphered_text)