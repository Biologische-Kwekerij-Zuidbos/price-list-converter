from platform import system
import subprocess

try:
    from os import getcwd
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
    win32api.ShellExecute(
        0,
        "print",
        getcwd() + file[1:],
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
