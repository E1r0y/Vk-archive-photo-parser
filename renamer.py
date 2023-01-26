import os

from sorter import sorted_aphanumeric


def rename():
    ext = ".html"
    path = '.\input'
    i = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    files = sorted_aphanumeric(os.listdir(path))
    try:
        for file in files:
            os.rename(os.path.join(path, file), os.path.join(path, str(i) + ext))
            i -= 1
    except FileExistsError:
        pass