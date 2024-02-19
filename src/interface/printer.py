from platform import system
import subprocess
import os

try:
    import win32api
    import win32print
except ImportError:
    pass

def print_files(files):
    if system() == 'Windows':
        for file in files:
            print_file_win(file)
    else:
        print('ERROR: %s system is not supported for printing' % system())

def print_file_win(file):
    os.system('start "excel" "%s"' % os.path.abspath(file))
