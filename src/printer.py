from platform import system
import subprocess

try:
    from os import startfile
except ImportError:
    pass

def print_files(files):
    if system() == 'Windows':
        for file in files:
            print_file_win(file)

def print_file_win(file):
    startfile(file, 'print')
