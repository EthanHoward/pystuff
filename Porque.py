import sys
import os
import time
import random
import string
from cryptography.fernet import Fernet

### vars / items ###

username_windows = os.environ["USERNAME"]

fernet_key = "'wxyNl0VBqzy7LoQuLfscsmO5ECix5rBZl6aTOdR-XGs='"

fernet_ciphersuite = Fernet(fernet_key)

msg_prefix = username_windows + "~#> "

encrypted_psw_file = open("psw.txt", "a+")
encrypted_usr_file = open("usr.txt", "a+")


encryped_userfromfile = encrypted_file.readline(1)

encryped_passwordfromfile = encrypted_file.readline(2)

### defs ###

time.sleep(5)

def cryptifier(string , status):
    time.sleep(5)
    if status == "enc":
        encoded_str = fernet_ciphersuite.encrypt(string)
        print(msg_prefix + "Encrypting...")
        return encoded_str
    if status == "dec":
        decoded_str = fernet_ciphersuite.decrypt(string)
        print(msg_prefix + "Decrypting...")
        return decoded_str
    else:
        print(msg_prefix + "Cryptifier failed")

def access_status(type):
    if type == True:
        print(msg_prefix + "###################################")
        print(msg_prefix + "######### Access Granted ##########")
        print(msg_prefix + "###################################")
    elif type == False:
        print(msg_prefix + "###################################")
        print(msg_prefix + "########## Access Denied ##########")
        print(msg_prefix + "###################################")
    else: 
        print(msg_prefix + "###################################")
        print(msg_prefix + "########## Access Failed ##########")
        print(msg_prefix + "###################################")
        
def login_script():
    print(msg_prefix + "###################################")
    print(msg_prefix + "############## Login ##############")
    print(msg_prefix + "###################################")    
    








if os.path.isfile("7d540d21-e1cc-4e3a-956a-306846a79b3e.txt"):
    login_script()
    username = input(msg_prefix + "Username:")
    password = input(msg_prefix + "Password:")
    if username == cryptifier(encrypted_file.readline(), "dec"):
        print("correct username")
else:
    print("File does not exist")
    time.sleep(5)
    