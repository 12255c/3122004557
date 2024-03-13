import unittest
import os
from main import read_file, lowercase, calculate_similarity


class TestPlagiarismDetection(unittest.TestCase):
    def test_read_file(self):
        # 测试文件的读写功能
        temp_file = 'temp_test_file.txt'
        with open(temp_file, 'w', encoding='utf-8') as file:
            file.write('testfile.')
        self.assertEqual(read_file(temp_file), 'testfile.')
        os.remove(temp_file)

    def test_none_file(self):
        self.assertEqual(read_file('invalid_file.txt'), FileNotFoundError)

    def test_translate(self):
        # 测试文件的预处理模块
        text = "testfile."
        preprocessed_text = lowercase(text)
        self.assertEqual(preprocessed_text, "testfile")

    def test_same(self):
        # 测试相同文本的相似度
        original_text = "Hello, world!"
        copied_text = "Hello, world!"
        self.assertEqual(calculate_similarity(lowercase(original_text), lowercase(copied_text)), 1)

    # 测试文本只有一半相同的情况
    def test_difference(self):
        original_text = "Hello, world!"
        copied_text = "Hello, universe!"
        self.assertAlmostEqual(calculate_similarity(lowercase(original_text), lowercase(copied_text)), 0.4615, places=4)

    # 测试文本完全不相同
    def test_total_difference(self):
        original_text = "Hello, world!"
        copied_text = "你好，世界！"
        self.assertAlmostEqual(calculate_similarity(lowercase(original_text), lowercase(copied_text)), 0)

    # 测试文本相似性很高
    def test_high_similarity(self):
        original_text = "This is a test."
        copied_text = "That is a test."
        self.assertAlmostEqual(calculate_similarity(lowercase(original_text), lowercase(copied_text)), 0.8182, places=4)

    # 测试文本相似性很低
    def test_low_similarity(self):
        original_text = "This is a test."
        copied_text = "This is a completely different test."
        self.assertAlmostEqual(calculate_similarity(lowercase(original_text), lowercase(copied_text)), 0.3667, places=4)

    # 测试其中一个文本为空的情况
    def test_empty_text(self):
        original_text = ""
        copied_text = "This is a test."
        self.assertEqual(calculate_similarity(lowercase(original_text), lowercase(copied_text)), 0)

    # 测试两个文本均为空
    def test_empty_text2(self):
        original_text = ""
        copied_text = ""
        self.assertEqual(calculate_similarity(lowercase(original_text), lowercase(copied_text)), -1)


if __name__ == "__main__":
    unittest.main()
