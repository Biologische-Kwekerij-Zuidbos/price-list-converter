import os
import subprocess


def print_files(files):
    for file in files:
        print_file_win(file)


def print_file_win(file):
    path = os.path.abspath(file)
    subprocess.check_call(['open', '-a', 'Microsoft Excel', path])
