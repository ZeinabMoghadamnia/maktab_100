from typing import List
import contextlib

def process_data(input_str: str) -> str:
    '''convert lower case to upper case'''
    processed_data = input_str.upper()
    return processed_data

@contextlib.contextmanager
def file_opener(file_path: str, mode: str):
    '''open file with choosed mode and yield file for close it'''
    with open(file_path, mode) as file:
        yield file

def main(input_file_path: str, output_file_path: str):
    '''get pathes and read file and write it after process'''
    with file_opener(input_file_path, 'r') as input_file:
        input_lines = input_file.readlines()

    output_data = []
    for line in input_lines:
        processed_line = process_data(line.strip())
        output_data.append(processed_line)

    with file_opener(output_file_path, 'w') as output_file:
        for item in output_data:
            output_file.write(f"{item}\n")

if __name__ == "__main__":
    input_file_path = "/home/zeinab/Documents/codes/maktab/Zeinab_Moghadamnia_HW8_maktab100/input.txt"
    output_file_path = "/home/zeinab/Documents/codes/maktab/Zeinab_Moghadamnia_HW8_maktab100/output.txt"

    main(input_file_path, output_file_path)
