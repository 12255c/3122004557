import unittest
from Myapp import generate_expression, is_valid


class TestMathScript(unittest.TestCase):
    def test_generate_expressions_and_answers(self):
        expression = "5+0"
        self.assertEqual(eval(expression),5)

    def test_division_by_zero(self):
        # 生成包含除以零操作的表达式
        expression = "5/0"
        self.assertFalse(is_valid(expression))

    def test_illegal_operator(self):
        # 包含非法操作符
        expression = "5^2"  # 强制将表达式设置为非法操作符
        self.assertFalse(is_valid(expression))

    def test_different_operators(self):
        expression = "3 + 5 * 2 - 4 / 2"  # 强制将表达式设置为3个以上运算符
        self.assertFalse(is_valid(expression))

    def test_empty_expression(self):
        expressions = ""
        self.assertFalse(is_valid(expressions))

    def test_single_number_expression(self):
        expression = "5"  # 强制将表达式设置为只包含一个数字
        self.assertFalse(is_valid(expression))

    def test_expression_with_variables(self):
        expression = "x + 5"  # 强制将表达式设置为包含变量
        self.assertFalse(is_valid(expression))

    def test_expression_with_negative_numbers(self):
        expression = "5 - 8"  # 强制将表达式结果设置为负数
        self.assertFalse(is_valid(expression))

    def test_single_operator_expression(self):
        expression = "*"  # 强制将表达式设置为只包含一个操作符
        self.assertFalse(is_valid(expression))

    def test_grammar_expression(self):
        expression = "-5 + 4"  # 强制将表达式设置为只包含一个操作符
        self.assertFalse(is_valid(expression))


if __name__ == '__main__':
    unittest.main()
