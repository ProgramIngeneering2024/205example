import ast

"""Модуль main.py: пример использования Pylint."""

user_input = input("Введите число: ")
number = ast.literal_eval(user_input)  # Безопасное преобразование
print(number * 2)