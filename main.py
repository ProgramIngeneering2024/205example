"""Модуль main.py: пример использования Pylint."""

# Пример уязвимости для Bandit (eval())
user_input = input("Введите выражение: ")

# pylint: disable=eval-used
eval(user_input)  # Bandit обнаружит это как уязвимость
