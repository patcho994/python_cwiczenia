def wybierz_figure():
    figura = input('Wybierz figurę (kwadrat, kolo, trojkat): ').lower()

    if figura == 'kwadrat':
        kwadrat()

    elif figura == 'kolo' or figura == 'koło':
        kolo()

    elif figura == 'trojkat' or figura == 'trójkąt':
        trojkat()
        
    else:
        print('Podano niewłaściwą figurę!')


def kwadrat():
    try:
        bok = float(input('Podaj dlugosc boku kwadratu w cm: '))
        if bok <=0:
            raise Exception()
        pole = bok * bok
        print(f'Pole kwadratu jest równe {pole}cm')
        
    except:
        wypisz_wyjatek()


def kolo():
    try:
        promien = float(input('Podaj promien kola w cm: '))
        if promien <= 0:
            raise Exception()
        pole = promien * 3.14 * promien
        print(f'Pole koła jest równe {pole}cm')
    except:
        wypisz_wyjatek()


def trojkat():
    try:
        wysokosc = float(input('Podaj wysokość trójkąta: '))
        podstawa = float(input('Podaj podstawę trójkąta: '))
        if wysokosc <= 0 or podstawa <= 0:
            raise Exception()
        pole = 0.5 * podstawa * wysokosc
        print(f'Pole trójkąta jest równe {pole}cm')
    except:
        wypisz_wyjatek()

def wypisz_wyjatek():
    print('Podano złą wartość!')


wybierz_figure()