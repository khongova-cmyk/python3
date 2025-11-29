while True:
    try:
        get_number = int(input("Enter a number: "))
        if get_number < 0:
            raise ValueError("Число не должно быть отрицательным!")
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте снова.")

while get_number >= 0:
    print(get_number)
    get_number -= 1
