age = int(input("Сколько вам лет? "))
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
