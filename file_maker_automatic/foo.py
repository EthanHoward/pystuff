import file_maker_auto 
import random, string

i = 0

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

while i < 50:
    file_maker_auto.file_maker(randomword(10000), 10000, randomword(7), 100)
    i = i + 1