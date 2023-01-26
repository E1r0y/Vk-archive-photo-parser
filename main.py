import os

from dowloader import downloader
from links_grabber import grabber
from renamer import rename


def main():
    print(''' __      ___  __                 _     _                   _           _                          _     _               
 \ \    / / |/ /                | |   (_)                 | |         | |                        | |   | |              
  \ \  / /| ' /    __ _ _ __ ___| |__  ___   _____   _ __ | |__   ___ | |_ ___     __ _ _ __ __ _| |__ | |__   ___ _ __ 
   \ \/ / |  <    / _` | '__/ __| '_ \| \ \ / / _ \ | '_ \| '_ \ / _ \| __/ _ \   / _` | '__/ _` | '_ \| '_ \ / _ \ '__|
    \  /  | . \  | (_| | | | (__| | | | |\ V /  __/ | |_) | | | | (_) | || (_) | | (_| | | | (_| | |_) | |_) |  __/ |   
     \/   |_|\_\  \__,_|_|  \___|_| |_|_| \_/ \___| | .__/|_| |_|\___/ \__\___/   \__, |_|  \__,_|_.__/|_.__/ \___|_|   
                                                    | |                            __/ |                                
                                                    |_|                           |___/                                 
''')
    input('Press Enter')
    rename()
    print('Файлы отсортированы.')
    amount = grabber()
    print(f'Найдено {amount} фото.')
    downloader()
    print(f'Фотографии находятся в /photo')
    input('Press Enter to close')


def clear():
    if os.sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    clear()
    main()
