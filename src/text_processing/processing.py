import pandas as pd
from tempfile import gettempdir
from pathlib import Path

import text_processing.list_style as ls
import text_processing.list_content as lc
import text_processing.text_wrapper as tw

def process_input_files(input_dirs, input_files):
    output_dirs = []

    for index, input_file in enumerate(input_files):
        # Concatenate all segments of the file into one DataFrame
        df = pd.concat(tuple(input_file))
        
        # Drop unnecessary columns so that
        # the page is not too wide for printing
        df.drop(columns=[3], inplace=True)

        # Fix row and column indices
        df.reset_index(drop=True, inplace=True)
        
        # Insert dates
        df = lc.insert_dates(df)
        # Style the DataFrame and get a Styler object
        styler = ls.style_dataframe(df)

        file_name=Path(input_dirs[index]).stem
        excel_file=gettempdir() + "/%s.xlsx" % file_name

        # Export as an Excel file
        styler.to_excel(
            excel_file,
            engine='openpyxl',
            index=False,
            header=False
        )

        # Wrap text (prevent overlapping of text)
        tw.wrap(excel_file)

        output_dirs.append(excel_file)
    
    return output_dirs
