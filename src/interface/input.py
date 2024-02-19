import pandas as pd
from platform import system
from tkinter import filedialog
from tkinter import Tk
from pathlib import Path

def get_downloads_path():
    return str(Path.home() / "Downloads")

def get_dirs():
    root = Tk()
    root.withdraw()
    root.filenames = filedialog.askopenfilenames(
        initialdir=get_downloads_path(),
        title="Select file(s)",
        filetypes=(("Excel files","*.xls"), ("All files","*.*"))
    )

    return root.filenames

def get_readings(dirs):
    return [pd.read_html(_dir) for _dir in dirs]