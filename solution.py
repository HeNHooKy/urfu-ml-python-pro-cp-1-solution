"""Функция, угадывающая заданное число от 1 до 100
"""
import numpy as np

def predict_number(number:int=np.random.randint(1, 101)) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток 
    """

    attempt_count = 0
    max_number = 100
    min_number = 0

    while True:
        attempt_count += 1
        current_prediction = (max_number - min_number) // 2 + min_number

        if number > current_prediction:
            min_number = current_prediction + 1
        elif number < current_prediction:
            max_number = current_prediction - 1
        else:
            break
    
    return attempt_count