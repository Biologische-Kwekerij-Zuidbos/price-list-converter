from platform import system
import os

def print_files(dirs):
    answer = input(
        'Print files? (y/n) '
    ).lower()

    if len(answer) > 0 and answer[0] == 'y':
        for output_dir in dirs:
            if system() == 'Windows':
                # Only use os.startfile on Windows system
                os.startfile(output_dir, 'print')