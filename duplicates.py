import os
import sys


def get_duplicates(path_to_folder):
    list_of_files = {}

    for path, dirs, filenames in os.walk(path_to_folder):
        for filename in filenames:
            if (filename in list_of_files) and (
                    os.path.getsize(os.path.join(path, filename)) ==
                    os.path.getsize(list_of_files[filename])
            ):
                print(os.path.join(path, filename))
                print(list_of_files[filename], end='\n\n')
            else:
                list_of_files[filename] = os.path.join(path, filename)


if __name__ == '__main__':
    try:
        get_duplicates(sys.argv[1])
    except IndexError:
        print(
            'Search path is not specified. '
            'Use "python duplicates.py <path_to_file>"'
        )
