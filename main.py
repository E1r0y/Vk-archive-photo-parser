import asyncio
import os

from funcs import downloader_async, grabber, rename_files


async def main():
    print(
        '''
 __      _ _  __                 _     _                   _           _                                        
 \ \    / / |/ /                | |   (_)                 | |         | |                                       
  \ \  / /| ' /    __ _ _ __ ___| |__  ___   _____   _ __ | |__   ___ | |_ ___    _ __   __ _ _ __ ___  ___ _ __ 
   \ \/ / |  <    / _` | '__/ __| '_ \| \ \ / / _ \ | '_ \| '_ \ / _ \| __/ _ \  | '_ \ / _` | '__/ __|/ _ \ '__|
    \  /  | . \  | (_| | | | (__| | | | |\ V /  __/ | |_) | | | | (_) | || (_) | | |_) | (_| | |  \__ \  __/ |   
     \/   |_|\_\  \__,_|_|  \___|_| |_|_| \_/ \___| | .__/|_| |_|\___/ \__\___/  | .__/ \__,_|_|  |___/\___|_|
                                                    | |                          | |                            
                                                    |_|                          |_|                            
                                                                                                        By @E1r0y
    '''
    )

    input("Press Enter")

    try:
        folder_name = rename_files()
    except (FileNotFoundError, ValueError) as err:
        print(err)
        input("Press Enter to close")
        return

    print("Файлы отсортированы.")
    amount = grabber(folder_name)
    print(f"Найдено {amount} фото.")

    if amount > 0:
        await downloader_async()
        print("Фотографии находятся в /photo")
    else:
        print("Ссылки на фото не найдены, загрузка пропущена.")

    input("Press Enter to close")


def clear():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    clear()
    asyncio.run(main())
