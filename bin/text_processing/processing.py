import pandas as pd
import os

import text_processing.list_style as ls
import text_processing.list_content as lc
import text_processing.text_wrapper as tw

def dir_to_file_name(_dir):
    return os.path.splitext(os.path.basename(_dir))[0]

def process_input_files(input_dirs, input_files):
    output_dirs = []

    for index, input_file in enumerate(input_files):
        # Concatenate all segments of the file into one DataFrame
        df = pd.concat(tuple(input_file))

        # Drop unnecessary column so that
        # the page is not too wide for printing
        df.drop(columns=[3], inplace=True)

        # Fix row and column indices
        df.reset_index(drop=True, inplace=True)
        
        # Insert dates
        df = lc.insert_dates(df)

        # Get the temp directory
        excel_dir = '../temp/' + dir_to_file_name(
            input_dirs[index]
        ) + '.xlsx'

        # Style the DataFrame and get a Styler object
        styler = ls.style_dataframe(df)

        # Export as an Excel file
        styler.to_excel(
            excel_dir,
            engine='openpyxl',
            index=False,
            header=False
        )

        # Wrap text (prevent overlapping of text)
        tw.wrap(excel_dir)

        output_dirs.append(excel_dir)
    
    return output_dirs
