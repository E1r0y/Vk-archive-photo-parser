import asyncio
import os
import re
from pathlib import Path

import aiohttp
from bs4 import BeautifulSoup
from tqdm import tqdm


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split(r"(\d+)", key)]
    return sorted(data, key=alphanum_key)


def rename_files(input_folder="./input", extension=".html"):
    base_path = Path(input_folder)
    folders = sorted([f for f in base_path.iterdir() if f.is_dir()], key=lambda p: p.name.lower())

    if not folders:
        raise FileNotFoundError(f"Не найдены папки в {input_folder}")

    if len(folders) > 1:
        raise ValueError(
            "Найдено несколько папок в input. Оставьте только одну папку с HTML-файлами диалога."
        )

    folder_path = folders[0]
    files = sorted_alphanumeric([f.name for f in folder_path.iterdir() if f.is_file()])

    if not files:
        raise FileNotFoundError(f"В папке {folder_path.name} нет файлов")

    # Переименование в 2 прохода, чтобы исключить конфликты имен.
    temp_paths = []
    for i, file_name in enumerate(reversed(files), start=1):
        old_path = folder_path / file_name
        temp_path = folder_path / f"__tmp__{i}{extension}"
        old_path.rename(temp_path)
        temp_paths.append((i, temp_path))

    for i, temp_path in temp_paths:
        final_path = folder_path / f"{i}{extension}"
        temp_path.rename(final_path)

    return folder_path.name


async def download_image(session, url, path, cnt, progress_bar):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            file_path = os.path.join(path, f"{cnt}.jpg")
            with open(file_path, "wb") as fd:
                content = await response.read()
                fd.write(content)
                progress_bar.update(1)
    except aiohttp.ClientError as e:
        print(f"Ошибка при загрузке изображения {url}: {e}")


async def download_images_from_file_async(session, file_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    total_images = len(lines)

    with tqdm(total=total_images, desc="Загрузка изображений", unit="image") as progress_bar:
        tasks = []
        for cnt, line in enumerate(lines, start=1):
            url = line.strip()
            if not url:
                continue
            tasks.append(download_image(session, url, output_folder, cnt, progress_bar))

        await asyncio.gather(*tasks)


async def downloader_async(path="./photo", links="links.txt"):
    if not os.path.exists(path):
        os.makedirs(path)
    async with aiohttp.ClientSession() as session:
        await download_images_from_file_async(session, links, path)


def grabber(folder_name):
    path = Path("./input") / folder_name
    html_files_count = len([f for f in path.iterdir() if f.is_file()])

    try:
        with open("links.txt", "w", encoding="utf-8") as links_file:
            for idx in range(1, html_files_count + 1):
                file_path = path / f"{idx}.html"
                if not file_path.exists():
                    continue

                with open(file_path, "r", encoding="utf-8") as html_file:
                    soup = BeautifulSoup(html_file.read(), "lxml")
                    links = soup.select('a[href^="https://sun"]')
                    for link in links:
                        href = link.get("href")
                        if href:
                            links_file.write(f"{href}\n")

        with open("links.txt", "r", encoding="utf-8") as links_file:
            summary = sum(1 for _ in links_file)
        return summary
    except FileNotFoundError:
        print("Фото не найдены.")
        return 0
