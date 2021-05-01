import os
import sys


f = open("num.txt", "a")

x = 1

while True:
        x = x + 1243456789 * x
        strX = str(x)
        print(strX)
        f.write(strX + "\n")

f.close()