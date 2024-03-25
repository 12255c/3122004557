import argparse
import random


# 生成题目以及答案列表
def generate_exercises(n, r):  # n为题目数量，r为运算数的范围
    exercises = []  # 题目列表
    answers = []  # 答案列表
    while len(exercises) < n:
        expression = generate_expression(r)
        if is_valid(expression):
            exercises.append(expression)
            answers.append(eval(expression))
    return exercises, answers


# 生成表达式
def generate_expression(r):
    # 由于运算符数量不定，需要特殊处理
    num_operators = random.randint(1, 3)
    num_operand = num_operators + 1

    operators = ['+', '-', '*', '/']
    operands = [random.randint(0, r) for _ in range(num_operand)]

    select_operator = random.sample(operators, num_operators)

    expression = ""  # 初始化一个空表达式
    expression += str(operands[0])

    for i in range(num_operators - 1):
        if select_operator[i + 1] == '/' and operands[i + 1] == 0:
            operands[i + 1] = random.randint(1, r)
            expression += str(select_operator[i + 1]) + " " + str(operands[i + 1]) + " "
        else:
            expression += str(select_operator[i + 1]) + " " + str(operands[i + 1]) + " "

    return expression


# 合法性判断
def is_valid(expression):
    try:
        if eval(expression) < 0:
            return False
    except ZeroDivisionError:
        return False
    return True  # 添加返回 True


# 保存题目和答案到文件中
def save_exercises_and_answers(exercises, answers):
    exercises_filename = r"C:\Users\98516\Desktop\3122004557\cowork\exercises.txt"
    answers_filename = r"C:\Users\98516\Desktop\3122004557\cowork\answers.txt"
    # 写入题目到Exercises.txt
    with open(exercises_filename, "w") as exercises_file:
        for i, exercise in enumerate(exercises, start=1):
            exercises_file.write(f"{i}. {exercise}\n")

    # 计算答案并写入到Answers.txt
    with open(answers_filename, "w") as answers_file:
        for i, answer in enumerate(answers, start=1):
            answers_file.write(f"{i}. {answer}\n")


def grade_answers(exercise_file, answer_file):
    exercises = load_file(exercise_file)
    answers = load_file(answer_file)

    correct_answers = []
    wrong_answers = []

    for i in range(len(answers)):
        if exercises[i].strip() == answers[i].strip():
            correct_answers.append(i + 1)
        else:
            wrong_answers.append(i + 1)

    return correct_answers, wrong_answers


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

# 保存得分到文件中
def save_grade(correct_answers, wrong_answers):
    grade_filename = r"C:\Users\98516\Desktop\3122004557\cowork\grade.txt"
    with open(grade_filename, "w") as grade_file:
        grade_file.write("Correct Answers:\n")
        for correct in correct_answers:
            grade_file.write(f"{correct}\n")
        grade_file.write("\nWrong Answers:\n")
        for wrong in wrong_answers:
            grade_file.write(f"{wrong}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='Number of exercises to generate', default=10)
    parser.add_argument('-r', type=int, help='Range of numbers in exercises', default=10)
    parser.add_argument('-e', '--exercisefile', type=str, help='Exercise file path')
    parser.add_argument('-a', '--answerfile', type=str, help='Answer file path')
    args = parser.parse_args()

    if args.exercisefile and args.answerfile:
        correct_answers, wrong_answers = grade_answers(args.exercisefile, args.answerfile)
        save_grade(correct_answers, wrong_answers)
    else:
        exercises, answers = generate_exercises(args.n, args.r)
        save_exercises_and_answers(exercises, answers)




