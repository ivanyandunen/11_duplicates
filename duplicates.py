import os
import sys
from collections import defaultdict


def get_all_files(path_to_folder):
    folder_content_dict = defaultdict(list)
    for path, dirs, filenames in os.walk(path_to_folder):
        for filename in filenames:
            filesize = os.path.getsize(os.path.join(path, filename))
            folder_content_dict[(filename, filesize)].append(
                os.path.join(path, filename)
            )
    return folder_content_dict


def print_duplicates(folder_content_dict):
    for elem in folder_content_dict:
        if len(folder_content_dict[elem]) > 1:
            print('File {} is duplicated: '.format(elem[0]))
            print('\n'.join(folder_content_dict[elem]))
            print('--------------------------------')


if __name__ == '__main__':
    try:
        if not os.path.exists(sys.argv[1]):
            print('Specified folder is not exist.')
    except IndexError:
        print(
            'Search path is not specified. '
            'Use "python duplicates.py <path_to_file>"'
        )
    else:
        folder_content_dict = get_all_files(sys.argv[1])
        print_duplicates(folder_content_dict)
