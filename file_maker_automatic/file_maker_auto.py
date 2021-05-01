import shutil
import os

def file_maker(_str_to_write_, _times_to_write_string_per_file, _filename_, _max_amount_):
    count = 1
    file_counter_safety = 1
    file_counter_safety_bool = True
    file_created_bool = False
    while count <= _max_amount_:
        
    
        filename_string = _filename_ + str(count) + ".txt"
        file_writing_to = open(filename_string, "a+")
        file_writing_to.write(_str_to_write_ * _times_to_write_string_per_file)
        print(filename_string)
        print(_str_to_write_ + " " + str(_times_to_write_string_per_file))
        file_writing_to.close()
        output_filenamager_string = _filename_ + " outputs " + str(file_counter_safety)
        if os.path.isdir(output_filenamager_string) & file_counter_safety_bool == True:
            file_counter_safety += 1
            file_counter_safety_bool = False
        elif file_created_bool == False:
            os.mkdir(output_filenamager_string)
            file_counter_safety_bool = False
            file_created_bool = True
        shutil.move(filename_string, output_filenamager_string)
        print("Moving " + filename_string + " to " + output_filenamager_string)
        count += 1


