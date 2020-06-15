from subprocess import Popen

import src.processing as proc
import src.input as inp
import src.printer as pr

input_dirs = inp.get_dirs()

print('Processing input files...')

output_dirs = proc.process_input_files(
    input_dirs,
    inp.get_readings(input_dirs)
)

inp.remove_files(input_dirs)

pr.print_files(output_dirs)

print('Done!')