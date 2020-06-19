from os import remove

from text_processing.processing import process_input_files
from interface.input import get_dirs, get_readings
from interface.printer import print_files

def remove_files(dirs):
    for _dir in dirs:
        remove(_dir)

input_dirs = get_dirs()

print('Processing input files...')

output_dirs = process_input_files(
    input_dirs,
    get_readings(input_dirs)
)

print_files(output_dirs)

remove_files(input_dirs)
remove_files(output_dirs)

print('Done!')