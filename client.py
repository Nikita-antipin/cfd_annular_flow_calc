import json
import os
from pathlib import Path


def open_test_data(filename: str) -> dict:
    """
    Открывает json файл с тестовыми данными
    :param filename: название файла, например, esp_data.json
    :return: словарь с данными
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(base_dir)
    file_test_path = os.path.join(test_data_path, filename)

    with open(file_test_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data
