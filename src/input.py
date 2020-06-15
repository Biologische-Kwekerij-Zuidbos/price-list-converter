import pandas as pd
import os

import src.user_input as uinp

def remove_files(dirs):
    if uinp.ask('Delete input files?'):
        for _dir in dirs:
            os.remove(_dir)

def get_dirs():
    # List all files in the 'input' directory
    dirs = os.listdir('./input')
    # Only select Excel files
    return [
        './input/' + _dir
        for _dir in dirs if _dir.endswith((
            '.xls',
            '.xlsx'
        )
    )]

def get_readings(dirs):
    return [pd.read_html(_dir) for _dir in dirs]