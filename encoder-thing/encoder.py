import base64
import os

msg_prefix = ">>"

output_file_name = ""

def initiate():
    option = input(msg_prefix + " 1. Encode 2. Decode: ")
    if option == "1":
        encode()
    elif option == "2":
        decode
    else:
        print(msg_prefix + " " + option + " is not an option, please press 1 or 2")
        initiate()



def encode():
    message = input(msg_prefix + "Enter what you want encoded:")
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64encode(message_bytes)
    write_to_file(b64_bytes, "encoded")
    
def decode():
    message_encrypted_file = input(msg_prefix + "Enter name of encoded .bin file:")
    read_binfile = open(message_encrypted_file, "rb").read()
    print(base64.b64decode(read_binfile))
    write_to_file(base64.b64decode(read_binfile), "decoded")




def write_to_file(str_to_write, save_encoded_or_decoded):
    count = 1
    if save_encoded_or_decoded == "encoded":
        filestr_enc = "out_encoded", count, ".txt"
        filestr_enc_sanitized = str(filestr_enc).replace(" ", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "")

        if os.path.isfile(filestr_enc_sanitized):
            count = count + 1
            print(msg_prefix + "")
        else:
            cascading_encoded_file = open(filestr_enc_sanitized, "a+")
            cascading_encoded_file.close
            encoded_bin_cascading = open(filestr_enc_sanitized, "rb")
            print(msg_prefix + "Outputted the encoded string to " + filestr_enc_sanitized + ".")
            encoded_bin_cascading.writeline(str(str_to_write))
            encoded_bin_cascading.close()
    elif save_encoded_or_decoded == "decoded":
        filestr_dec = "out_decoded", count, ".txt"
        filestr_dec_sanitized = str(filestr_dec).replace(" ", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "")

        if os.path.isfile(filestr_dec_sanitized):
            count = count + 1
            print(msg_prefix + "")
        else:
            cascadong_decoded_file = open(filestr_dec_sanitized, "a+")
            print(msg_prefix + "Outputted the encoded string to " + filestr_dec + ".")
            cascadong_decoded_file.writeline(str(str_to_write))
            cascadong_decoded_file.close()
initiate()