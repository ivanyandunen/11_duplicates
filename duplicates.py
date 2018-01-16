import os
import sys


def print_duplicates(duplicate1, duplicate2):
    print(
        'The file:\n{}\nis duplicated by the file:\n{}'.format(
            duplicate1,
            duplicate2
        ),
        end='\n\n'
    )


def find_duplicates(path_to_folder):
    folder_content = {}

    for path, dirs, filenames in os.walk(path_to_folder):
        for filename in filenames:
            if (filename in folder_content) and (
                    os.path.getsize(os.path.join(path, filename)) ==
                    os.path.getsize(folder_content[filename])
            ):
                print_duplicates(
                    os.path.join(path, filename),
                    folder_content[filename]
                )

            else:
                folder_content[filename] = os.path.join(path, filename)


if __name__ == '__main__':
    try:
        find_duplicates(sys.argv[1])
    except IndexError:
        print(
            'Search path is not specified. '
            'Use "python duplicates.py <path_to_file>"'
        )
