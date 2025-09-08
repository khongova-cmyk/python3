def max_number(a, b):
    if a > b:
        return a
    return b
print(max_number(1, 2))

def empty_function():
    pass
print(empty_function())

def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
print(list(even_numbers(10)))

def test_max_number():

    assert max_number(5, 3) == 5, "Ошибка: max_number(5, 3) должно быть 5"
    assert max_number(2, 8) == 8, "Ошибка: max_number(2, 8) должно быть 8"
    assert max_number(-1, 5) == 5, "Ошибка: max_number(-1, 5) должно быть 5"

    assert max_number(7, 7) == 7, "Ошибка: max_number(7, 7) должно быть 7"
    assert max_number(0, 0) == 0, "Ошибка: max_number(0, 0) должно быть 0"

    assert max_number(-3, -5) == -3, "Ошибка: max_number(-3, -5) должно быть -3"

    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    test_max_number()

    print("\nЧетные числа до 10:")
    for num in even_numbers(10):
        print(num, end =" ")

    print("\n\nПустая функция ничего не выводит:")
    empty_function()