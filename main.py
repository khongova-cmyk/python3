def get_number():
    while True:
        try:
            num = int(input("Введите число от 1 до 5: "))
            if 1 <= num <= 5:
                return num
            else:
                print("Число должно быть от 1 до 5. Попробуйте снова.")
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")


number_words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

number = get_number()

print(f"Число {number} на английском: {number_words[number]}")
