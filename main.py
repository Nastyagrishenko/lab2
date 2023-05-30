def first():
    password1 = str(input())
    password2 = str(input())

    if password1 != password2:
        print('Пароль не принят')
    else:
        print('Пароль принят')


def second():
    place = int(input())

    if place > 54:
        pass
    elif place > 36 and place % 2 == 0:
        print('Боковое верхнее')
    elif place > 36 and place % 2 != 0:
        print('Боковое нижнее')
    elif place % 2 != 0:
        print('Нижнее место в купе')
    elif place % 2 == 0:
        print('Верхнее место в купе')


def third():
    year = int(input())

    if year % 4 == 0:
        print(f'{year} год високосный')
    else:
        print(f'{year} год не високосный')


def fourth():
    color1, color2 = str(input()), str(input())
    if (color1.lower() == 'красный' and color2.lower() == 'синий') or (color2.lower() == 'красный' and color1.lower() == 'синий'):
        print('фиолетовый')
    elif (color1.lower() == 'жёлтый' and color2.lower() == 'синий') or (color2.lower() == 'жёлтый' and color1.lower() == 'синий'):
        print('зелёный')
    elif (color1.lower() == 'жёлтый' and color2.lower() == 'красный') or (color2.lower() == 'жёлтый' and color1.lower() == 'красный'):
        print('оранжевый')
    else:
        print('ошибка')


def fifth():
    n = int(input('Выберите количество слов, которое будете вводить: '))
    s = []

    for i in range(1, n + 1):
        a = input()
        s.append(a)

    print(*s)
