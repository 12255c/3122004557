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
    return FileNotFoundError


def lowercase(text):
    # 去除文本当中的标点符号并将文本小写
    try:
        text = text.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '')
        return text
    except Exception as e:
        print(f'处理文本时发生错误：{e}')
        return None


def calculate_similarity(original_text, copied_text):
    # 计算两个文本的相似度
    matcher = difflib.SequenceMatcher(None, original_text, copied_text)
    matching_blocks = matcher.get_matching_blocks()
    matching_amount = sum(block.size for block in matching_blocks)
    if max(len(original_text), len(copied_text)) != 0:
        copy_percentage = matching_amount / max(len(original_text), len(copied_text))
        return copy_percentage

    return -1


def main():
    # 主函数。处理命令行输入，读取文件，计算相似度，并输出结果。
    # 检查命令行参数
    if len(sys.argv) != 4:
        print("用法：python main.py 原文文件路径 抄袭文件路径 输出文件路径")
        sys.exit(1)
    # 获取文件路径
    original_path, copied_path, output_path = sys.argv[1:]
    # 读取文件内容
    original_text = read_file(original_path)
    copied_text = read_file(copied_path)
    # 文本预处理
    original_text = lowercase(original_text)
    copied_text = lowercase(copied_text)
    # 计算查重率
    similarity_percentage = calculate_similarity(original_text, copied_text)
    if similarity_percentage == -1:  # 异常标识-1
        with open(output_path, 'a', encoding="utf_8") as output_file:
            output_file.write("ERROR")
        return
    # 写入输出文件
    with open(output_path, 'w', encoding="utf_8") as output_file:
        output_file.write(f"{similarity_percentage:.2%}")


if __name__ == "__main__":
    main()
