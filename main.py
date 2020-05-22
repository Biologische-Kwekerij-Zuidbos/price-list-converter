import pandas as pd
import os
import list_style as ls

def dir_to_file_name(dir):
    return os.path.splitext(os.path.basename(dir))[0]

# List all files in the 'input' directory
input_dirs = os.listdir('./input')
# Only select Excel files
input_dirs = ['./input/' + input_dir for input_dir in input_dirs if input_dir.endswith((
    '.xls',
    '.xlsx'
))]

input_files = [pd.read_html(input_dir) for input_dir in input_dirs]

for index, input_file in enumerate(input_files):
    # Style the input file
    # style_file(input_file)
    
    # Convert the html reading of the file to a .csv file
    df = pd.concat(tuple(input_file))
    df.reset_index(drop=True, inplace=True)
    df.style \
        .apply(ls.color_rows, axis=0) \
        .apply(ls.color_head, axis=0) \
        .apply(ls.color_head_text, axis=0) \
        .set_properties(
            **{'width': '600px'},
            inplace=True
        ) \
        .to_excel(
            # Use same name as the corresponding input file and substitute .csv file type
            './output/' + dir_to_file_name(input_dirs[index]) + '.xlsx',
            engine='openpyxl'
        )