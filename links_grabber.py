import os

from bs4 import BeautifulSoup


def grabber():
    path = '.\input'
    count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    z = 0
    try:
        with open('links.txt', 'w') as y:
            for i in range(count):
                z = z + 1
                with open(f'{path}\{z}.html', 'r') as x:
                    soup = BeautifulSoup(x, 'html.parser')
                    links = soup.select('a[href^="https://sun"]')
                    for link in links:
                        x = link.get('href')
                        y.write(f'{x}\n')
        summary = sum(1 for line in open('links.txt', 'r'))
        return summary
    except Exception:
        print('Что-то пошло не так, проверьте файлы в папке links')
