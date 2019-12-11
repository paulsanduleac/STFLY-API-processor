from itertools import product
from string import ascii_lowercase, digits
# generate API UUIDs
# 8 characters + 4 characters + 4 characters + 4 characters + 12 characters
for i in product(ascii_lowercase + digits, repeat=33):
        word = ""
        for letter in i:
            word+=str(letter)
        uuid=word[0:8]+"-"+word[8:12]+"-"+word[12:16]+"-"+word[16:20]+"-"+word[20:32]
