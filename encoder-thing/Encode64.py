import os
import base64

cmd_prefix = ">>"

def init():
    enc_dec_input = input(cmd_prefix + "1. Encode 2. Decode ")



def encode(string_to_encode):
    save_or_exit_input = input("1. Save to file 2. Exit")
    decoded_to_encode_string = input(cmd_prefix + "Input string to be encoded: ")
    encoded_string = base64.b64encode(decoded_to_encode_string)
    print(encoded_string)
    if save_or_exit_input == "1":
        file_mgr(encoded_string, "write")
    elif save_or_exit_input == "2":
        exit()

def file_mgr(string_import, read_or_write):
    if read_or_write == "write":
        file_name_input_saving = input(cmd_prefix + "Input filename to save as: ")
        file_name = file_name_input + ".txt"
        file_unencoded = open(file_name, "a+")
        file_unencoded.writeline(string_import)
    elif read_or_write == "read":
        file_name_input_open = input(cmd_prefix + "Input filename to open: ")
        if file_name_input_open.__contains__(".txt"):
            