import math

# Длина рва в метрах
length_of_trench = 1400

# Длина, которую один землекоп может выкопать за день
length_per_day = 3

# Количество рабочих, необходимых для выкопки
days = math.ceil(length_of_trench / (length_per_day * 2))

print("Количество дней, необходимых для выкопки рва:", days)