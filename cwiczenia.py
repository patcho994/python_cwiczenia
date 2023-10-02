def dodaj(pierwsza, druga):
    wynik = pierwsza + druga
    print(wynik)

def odejmij(pierwsza, druga):
    wynik = pierwsza - druga
    print(wynik)

def pomnoz(pierwsza, druga):
    wynik = pierwsza * druga
    print(wynik)

def podziel(pierwsza, druga):
    wynik = pierwsza / druga
    print(wynik)


def start():
    try:
        pierwsza = float(input('Podaj pierwszą liczbę: '))
        druga = float(input('Podaj drugą liczbę: '))
        znak = input('Podaj znak matematyczny: ')
        if znak == '+':
            dodaj(pierwsza, druga)
        elif znak == '-':
            odejmij(pierwsza, druga)
        elif znak == '*':
            pomnoz(pierwsza, druga)
        elif znak == '/':
            if druga == 0:
                print('Nie dzielimy przez 0')
            else:
                podziel(pierwsza, druga)
        else:
            print('Niewłaściwy znak')

    except:
        print('Wprowadzono nieprawidlowe dane')

start()