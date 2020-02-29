"""
а) Дано символи - s1, s2, .... Відомо, що символ s1 відмінний від пробілу і що серед
s2, s3, ... є хоча б один пробіл. Розглядаються s1, ..., sn - символи, що передують першому
пробілу (n заздалегідь не відомо). З послідовності s1, ..., sn сформувати множину, в якій
видалити всі символи, що не є буквами або цифрами, і замінити кожну велику букву на
однойменну малу.
Barbak Vladuslav 122V
"""
while True:
    a=input('Input symbol: ')
    s=set()
    if a[0]!=' ':
        new_a=a.lower()
        for i in new_a:
            if i==' ':
                break
            if i.isalpha() or i.isdigit():
                s.add(i)
        print(s)
    else:
        print('First symbol is not a space')
    result = input('Want to restart? If yes - 1, No - other: ')
    if result == '1':
        continue
    else:
        break