year_of_born = int(input('Пожалуйста, введите год рождения А.С.Пушкина: '))


if year_of_born == 1799:
    date_of_born = input('А какой день его рождения? ')
    if date_of_born == '6 июня':
        print('Верно!')
    else:
        print('Неверный день рождения!')
else:
    print('Неверный год рождения!')