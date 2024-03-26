import argparse
import os
import random
from fractions import Fraction


# 生成题目时至少包含一个运算符
def generate_expression(r):
    # 由于运算符数量不定，需要特殊处理
    num_operators = random.randint(1, 3)
    num_operand = num_operators + 1

    operators = ['+', '-', '*', '/']
    operands = [random.randint(0, r) for _ in range(num_operand)]

    select_operator = random.sample(operators, num_operators)

    expression = ""  # 初始化一个空表达式
    expression += str(operands[0]) + " "

    for i in range(num_operators):
        expression += str(select_operator[i]) + " " + str(operands[i + 1]) + " "

    return expression


# 生成题目以及答案列表
"""def generate_exercises(exercises, answers, n, r):
    while len(exercises) < n:
        expression = generate_expression(r)
        if is_valid(expression):
            exercises.append(expression)
            answers.append(eval(expression))"""


def generate_exercises(exercises, answers, n, r):
    while len(exercises) < n:
        expression = generate_expression(r)
        if is_valid(expression):
            exercises.append(expression)
            answer = eval(expression)
            fraction = Fraction(answer).limit_denominator()  # 将答案转换为真分数
            whole_part = fraction.numerator // fraction.denominator  # 获取整数部分
            numerator = abs(fraction.numerator) % fraction.denominator  # 获取真分数的分子（取绝对值）
            denominator = fraction.denominator  # 获取真分数的分母
            if numerator == 0:  # 如果分子为0
                if whole_part == 0:  # 如果整数部分也为0
                    answers.append("0")  # 答案为0
                else:  # 如果整数部分不为0
                    answers.append(f"{whole_part}")  # 只输出整数部分
            else:  # 如果分子不为0
                if whole_part == 0:  # 如果整数部分为0
                    answers.append(f"{numerator}/{denominator}")  # 答案直接为真分数
                else:  # 如果整数部分不为0
                    answers.append(f"{whole_part}'{numerator}/{denominator}")


# 保存题目和答案到文件中
def save_exercises_and_answers(exercises, answers, script_dir):
    exercise_file = os.path.join(script_dir, "exercises.txt")
    answer_file = os.path.join(script_dir, "answers.txt")

    with open(exercise_file, "w") as exercises_file:
        for i, exercise in enumerate(exercises, start=1):
            exercises_file.write(f"{i}. {exercise}\n")

    with open(answer_file, "w") as answers_file:
        for i, answer in enumerate(answers, start=1):
            answers_file.write(f"{i}. {answer}\n")


# 合法性判断
def is_valid(expression):
    try:
        if eval(expression) < 0:
            return False
    except ZeroDivisionError:
        return False
    return True


def grade_answers(exercise_file, answer_file):
    check_exercises = load_file(exercise_file)
    check_answers = load_file(answer_file)

    correct_answers = []
    wrong_answers = []

    for i in range(len(check_answers)):
        if check_exercises[i].strip() == check_answers[i].strip():
            wrong_answers.append(i + 1)
        else:
            correct_answers.append(i + 1)

    return correct_answers, wrong_answers


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()


# 保存得分到文件中
def save_grade(correct_answers, wrong_answers, script_dir):
    total_correct = len(correct_answers)
    total_wrong = len(wrong_answers)

    grade_file_path = os.path.join(script_dir, "grade.txt")

    with open(grade_file_path, "w") as grade_file:
        grade_file.write(f"Correct: {total_correct}\n")

        if total_correct > 0:
            grade_file.write("(")
            for idx, correct in enumerate(correct_answers, start=1):
                grade_file.write(f"{correct},")
            grade_file.write(")\n")

        grade_file.write(f"Wrong: {total_wrong}\n")

        if total_wrong > 0:
            grade_file.write("(")
            for idx, wrong in enumerate(wrong_answers, start=1):
                grade_file.write(f"{wrong},")
            grade_file.write(")\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='Number of exercises to generate', default=10)
    parser.add_argument('-r', type=int, help='Range of numbers in exercises', default=10)
    parser.add_argument('-e', '--exercisefile', type=str, help='Exercise file path')
    parser.add_argument('-a', '--answerfile', type=str, help='Answer file path')
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.realpath(__file__))

    exercises = []
    answers = []

    if args.exercisefile and args.answerfile:
        correct_answers, wrong_answers = grade_answers(args.exercisefile, args.answerfile)
        save_grade(correct_answers, wrong_answers, script_dir)
    else:
        generate_exercises(exercises, answers, args.n, args.r)
        save_exercises_and_answers(exercises, answers, script_dir)
