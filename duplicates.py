import os
import sys
from collections import defaultdict


def get_all_files(path_to_folder):
    folder_content = defaultdict(list)
    for path, dirs, filenames in os.walk(path_to_folder):
        for filename in filenames:
            filesize = os.path.getsize(os.path.join(path, filename))
            folder_content[(filename, filesize)].append(
                os.path.join(path, filename)
            )
    return folder_content


def print_duplicates(folder_content):
    for elem in folder_content:
        if len(folder_content[elem]) > 1:
            print('Files are duplicated: ')
            print('\n'.join(folder_content[elem]))
            print('--------------------------------')


if __name__ == '__main__':
    try:
        folder_content = get_all_files(sys.argv[1])
        print_duplicates(folder_content)
    except IndexError:
        print(
            'Search path is not specified. '
            'Use "python duplicates.py <path_to_file>"'
        )
