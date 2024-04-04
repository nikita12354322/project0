import numpy as np
def game_core_v2(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    start = 1  # присваиваем значение, соответствующее нижней границе диапазона поиска
    stop = 101  # присваиваем значение, соответствующее верхней границе диапазона поиска +1

    while True:
        average_number = (start + stop)//2
        count += 1
        if average_number == number:
            break  # выход из цикла если угадали
        elif number > average_number:
            start = average_number  # перезаписываем переменную start,чтобы уменьшить диапазон поиска числа => меньше
        else:
            stop = average_number # перезаписываем переменную high

    return count
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
if __name__ == "__main__":
    # RUN
    score_game(game_core_v2)