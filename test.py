"""Игра - угадай число!"""

import numpy as np

def game(number: int = 1) -> int: 
    count = 0
    min, max = 1, 100 #Задаем границы минимума и максимума,а также середину диапазона поиска
    number_predict = max / 2
    
    while number != number_predict:#Цикл уменьшает радиус поиска после каждого выполненного условия
        count+=1
 
        if number > number_predict: 
            min = number_predict
            number_predict = round((max + min) / 2)
        elif number < number_predict: 
            max = number_predict
            number_predict = round((max + min) / 2)
        while number != number_predict:
            if number > number_predict:
                min = number_predict
                number_predict = round((max + min) / 2)
            elif number < number_predict: 
                max = number_predict
                number_predict = round((max + min) / 2)
                                                                   
    return count

values_count = game(int(np.random.randint(1, 101)))
print(f"Ваш код угадал загаданное число за {values_count} попыток")
# Конец игры