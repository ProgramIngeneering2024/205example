# Пример уязвимости для Bandit (eval())
user_input = input("Введите выражение: ")
eval(user_input)  # Bandit обнаружит это как уязвимость