from os import remove

import text_processing.processing as proc
import interface.input as inp
import interface.printer as pr

def remove_files(dirs):
    for _dir in dirs:
        remove(_dir)

input_dirs = inp.get_dirs()

print('Processing input files...')

output_dirs = proc.process_input_files(
    input_dirs,
    inp.get_readings(input_dirs)
)

pr.print_files(output_dirs)

#remove_files(input_dirs)
#remove_files(output_dirs)

print('Done!')