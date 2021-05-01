import shutil
import time
import sys
import WConio2
import os
from prompter import yesno

# variables #

msg_prefix = ">"

i = 0

space_indentation = 0

# methods #

# yes/no prompt #
def yes_no():
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
     
    while True:
        choice = input('Again? [Y/N]?' + '\n' + msg_prefix).lower()
        if choice in yes:
           time.sleep(0.3)
           return True
        elif choice in no:
           time.sleep(0.3)
           return False
        else:
           print('Please respond with yes or no\n' + msg_prefix)


# this method takes two numbers, length is the length of the whole string, 
# it's the same as the length on pyramid_maker, string_length is the length of the string of string_main_character, 
# and string_spacer is whatever you put as string_spacer on pyramid_maker, for example pyramid_maker(".", "#", 100),
# the "." is the string_spacer, the "#" is the string_main character and the 100 is the size of the lines
# so, you will use space_calculator(len(main_string_storage), ".", 100), the 100 is actually passed as "length" in main
def space_calculator(string_length, string_spacer, length):
    space_size_part1 = length - string_length
    space_size = int(space_size_part1/2)
    space_calculated = str(string_spacer * space_size)
    return space_calculated
    

def pyramid_maker(string_spacer, string_main_character, length):    
    
    line_num = 0 

    main_string_storage = (string_main_character + string_main_character)

    print(string_spacer * length)

    while i < length: 
        line_num += 1
        main_string_storage_length = int(len(main_string_storage))
        space_calculated_local = str(space_calculator(main_string_storage_length, string_spacer, length))
        i + 2
        print(space_calculated_local + main_string_storage + space_calculated_local)
        main_string_storage += (string_main_character + string_main_character)
        time.sleep(0.03)
        if main_string_storage_length >= length:
            local_vertical_printed_string = " Lines printed vertically: " + str(line_num) + " "
            local_vertical_printed_string_length = len(local_vertical_printed_string)
            print(space_calculator(local_vertical_printed_string_length, string_spacer, length) + local_vertical_printed_string + space_calculator(local_vertical_printed_string_length, string_spacer, length))
            while True:
                if yes_no() == False:
                    print(msg_prefix + "Exiting...")
                    exit()
                else:
                    print(".")
                    os.system("cls")
                    print("..")
                    os.system("cls")
                    print("...")
                    os.system("cls")
                    initiate()


def initiate():
    os.system("cls")
    print("Entering a single space for the characters will work and lengths over ~300 can go wrong")
    string_spacer_input = input("Please type the spacer character" + msg_prefix)
    string_main_char_input = input("Please type the main character" + msg_prefix)
    string_length_main_input = int(input("Please type the length of the string" + msg_prefix))
    os.system("cls")
    while True:
        pyramid_maker(string_spacer_input, string_main_char_input, string_length_main_input)


initiate()