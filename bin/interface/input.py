import pandas as pd
from platform import system
from tkinter import filedialog
from tkinter import Tk

def get_dirs():
    _initialdir = 'C:/Downloads'
    if system() != 'Windows':
        _initialdir = '../temp'

    root = Tk()
    root.withdraw()
    root.filenames = filedialog.askopenfilenames(
        initialdir=_initialdir,
        title="Select file(s)",
        filetypes=(("Excel files","*.xls"), ("All files","*.*"))
    )

    return root.filenames

def get_readings(dirs):
    return [pd.read_html(_dir) for _dir in dirs]