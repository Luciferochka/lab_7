"""
б) Задача. Визначити середній бал оцінок з усіх предметів, і вивести відомості про
студентів, середній бал яких складає більше 75б. Поля структури: Прізвище, Група,
Фізика, Алгоритмізація та програмування, Вища математика.
"""
while True:
    data = [{'Mysorov': 'Screentolik', 'Група': '122G', 'Physics': 85, 'Algorithmization and programming': 99,
             'Higher mathematics': 95},
            {'Torchkov': 'Pedros', 'Група': '122G', 'Physics': 53, 'Algorithmization and programming': 75,
             'Higher mathematics': 77},
            {'Kruvorychko': 'Panas', 'Група': '122G', 'Physics': 80, 'Algorithmization and programming': 67,
             'Higher mathematics': 82},
            {'Hrupluviy': 'Ivan', 'Група': '122G', 'Physics': 68, 'Algorithmization and programming': 77,
             'Higher mathematics': 90},
            ]
    output = []
    for i in data:
        average_mark = (i.get('Physics') + i.get('Algorithmization and programming') + i.get('Higher mathematics'))/3
        if average_mark > 75:
            output.append(i)
    print("Nice students: ")
    for student in output:
        print(f'{student}')

    result = input('Want to restart? If yes - 1, No - other: ')
    if result == '1':
        continue
    else:
        break
