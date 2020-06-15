import pandas as pd
import os
from tkinter import filedialog
from tkinter import Tk

def get_dirs():
    return filedialog.askopenfilenames(
        initialdir="C:/Downloads",
        title="Select file(s)",
        filetypes=(("Excel files","*.xls"), ("All files","*.*"))
    )

def get_readings(dirs):
    return [pd.read_html(_dir) for _dir in dirs]