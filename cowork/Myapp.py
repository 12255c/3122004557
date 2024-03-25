import argparse
import os
import random


# 生成题目时至少包含一个运算符
def generate_exercise(min_operators=1):
    operators = ['+', '-', '*', '/']
    num_operators = random.randint(min_operators, 3)
    exercise = str(random.randint(1, 100))
    for _ in range(num_operators):
        operator = random.choice(operators)
        operand = str(random.randint(1, 100))
        exercise += f' {operator} {operand}'
    return exercise


# 生成题目文件
def generate_exercise_file(filename, num_exercises, min_operators=1):
    with open(filename, 'w') as file:
        for _ in range(num_exercises):
            exercise = generate_exercise(min_operators)
            file.write(exercise + '\n')


# 生成题目以及答案列表
def generate_exercises(n, r):
    exercises = []
    answers = []
    while len(exercises) < n:
        expression = generate_exercise()
        if is_valid(expression):
            exercises.append(expression)
            answers.append(eval(expression))
    return exercises, answers


# 保存题目和答案到文件中
def save_exercises_and_answers(exercises, answers, directory):
    exercises_filename = os.path.join(directory, r"C:\Users\98516\Desktop\3122004557\cowork\Exercises.txt")
    answers_filename = os.path.join(directory, r"C:\Users\98516\Desktop\3122004557\cowork\answers.txt")

    with open(exercises_filename, "w") as exercises_file:
        for i, exercise in enumerate(exercises, start=1):
            exercises_file.write(f"{i}. {exercise}\n")

    with open(answers_filename, "w") as answers_file:
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
    exercises = load_file(exercise_file)
    answers = load_file(answer_file)

    correct_answers = []
    wrong_answers = []

    for i in range(len(answers)):
        if exercises[i].strip() == answers[i].strip():
            wrong_answers.append(i + 1)
        else:
            correct_answers.append(i + 1)

    return correct_answers, wrong_answers


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()


# 保存得分到文件中
def save_grade(correct_answers, wrong_answers, directory):
    grade_filename = os.path.join(directory, r"C:\Users\98516\Desktop\3122004557\cowork\grade.txt")
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
    parser.add_argument('-d', '--directory', type=str, help='Directory to save files', default='.')
    parser.add_argument('-e', '--exercisefile', type=str, help='Exercise file path')
    parser.add_argument('-a', '--answerfile', type=str, help='Answer file path')
    args = parser.parse_args()

    if args.exercisefile and args.answerfile:
        correct_answers, wrong_answers = grade_answers(args.exercisefile, args.answerfile)
        save_grade(correct_answers, wrong_answers, args.directory)
    else:
        exercises, answers = generate_exercises(args.n, args.r)
        save_exercises_and_answers(exercises, answers, args.directory)
