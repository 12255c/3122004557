import difflib
import string
import sys


def read_file(path):
    # 读取文件
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f'文件不存在：{path}')
        return FileNotFoundError
    