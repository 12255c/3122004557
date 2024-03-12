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
    except Exception as e:
        print(f'读取文件时发生错误：{e}')
    return None


def remove_punctuation_and_lowercase(text):
    # 去除文本当中的标点符号并将文本小写
    try:
        text = text.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '')
        return text
    except Exception as e:
        print(f'处理文本时发生错误：{e}')
        return None


def main():


if __name__ == "__main__":
    main()
