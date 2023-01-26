import time

import requests


def downloader():
    path = '.\photo'
    summary = sum(1 for line in open('links.txt', 'r'))
    with open('links.txt', 'r') as f:
        line = f.readline()
        cnt = 0
        try:
            while line:
                x = line.strip()
                line = f.readline()
                cnt += 1
                r = requests.get(x, stream=True)
                with open(f'{path}\{cnt}.jpg', 'wb') as fd:
                    print(f'{cnt}/{summary}')
                    for chunk in r.iter_content():
                        fd.write(chunk)
        except TimeoutError:
            print('Задержка ответа от сервера, ожидайте')
            time.sleep(5)
            pass
