def max_number(a, b):
    if a > b:
        return a
    return b


def empty_function():
    pass


def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


def test_max_number():
    assert max_number(5, 3) == 5, "Ошибка: первое число должно быть больше"

    assert max_number(2, 8) == 8, "Ошибка: второе число должно быть больше"

    assert max_number(7, 7) == 7, "Ошибка: равные числа должны возвращать любое из них"

    assert max_number(-3, -5) == -3, "Ошибка: должно вернуться большее отрицательное число"

    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    test_max_number()

    print("\nЧетные числа до 10:")
    for num in even_numbers(10):
        print(num, end=" ")
        
    print("\n\nПустая функция ничего не выводит:")
    result = empty_function()
    print("Результат пустой функции:", result)
