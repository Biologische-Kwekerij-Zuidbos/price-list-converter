import pandas as pd
from os import path

import src.list_style as ls
import src.list_content as lc
import src.text_wrapper as tw

def dir_to_file_name(dir):
    return path.splitext(path.basename(dir))[0]

def process_input_files(input_dirs, input_files):
    output_dirs = []

    for index, input_file in enumerate(input_files):
        # Concatenate all segments of the file into one DataFrame
        df = pd.concat(tuple(input_file))

        # Fix row and column indices
        df.reset_index(drop=True, inplace=True)
        
        # Insert dates
        df = lc.insert_dates(df)

        # Get the output directory
        output_dir = './output/' + dir_to_file_name(
            input_dirs[index]
        ) + '.xlsx'

        # Style the DataFrame and export it
        ls.style_dataframe(df).to_excel(
            # Use same name as the corresponding input file
            # and substitute .csv file type
            output_dir,
            engine='openpyxl',
            index=False,
            header=False
        )

        # Wrap text (prevent overlapping of text)
        tw.wrap(output_dir)

        output_dirs.append(output_dir)
    
    return output_dirs
