def get_age():
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            if age < 0:
                print("Возраст не может быть отрицательным. Попробуйте снова.")
                continue
            return age
        except ValueError:
            print("Ошибка! Пожалуйста, введите число для возраста.")

age = get_age()

citlizen = input("Вы гражданин страны? (Да\Нет)").lower().strip()
disqualified = input("Вы зек? (Да\Нет)").lower().strip()

if age >= 18 and citlizen == "да" and disqualified == "нет":
    print("Вы можете голосовать на выборах!")
else:
    print("Вы не можете голосовать на выборах.")

    if age < 18:
        print("- Ваш возраст меньше 18 лет")
    if citlizen != "да":
        print("- Вы не являетесь гражданином страны")
    if disqualified != "нет":
        print("- Вы дисквалифицированы")
