import pandas as pd
import os
import platform

import src.processing as proces
import src.printer as printer

# List all files in the 'input' directory
input_dirs = os.listdir('./input')
# Only select Excel files
input_dirs = [
    './input/' + input_dir
    for input_dir in input_dirs if input_dir.endswith((
        '.xls',
        '.xlsx'
    )
)]

input_files = [pd.read_html(input_dir) for input_dir in input_dirs]

print('Processing input files...')

output_dirs = proces.process_input_files(
    input_dirs,
    input_files
)

print('Done!')

printer.print_files(output_dirs)
