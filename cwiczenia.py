# def czy_parzysta():
#     liczba = int(input('Podaj liczbe: '))
    # if liczba % 2 == 0:
    #     print('Jest parzysta')
    # elif liczba % 2 == 1:
    #     print('Jest nieparzysta')
#     else:
#         print('Nie podano liczby')

# czy_parzysta()

def czy_parzysta():
    try:
        liczba = int(input('Podaj liczbe: '))
        if liczba % 2 == 0:
            print('Jest parzysta')
        elif liczba % 2 == 1:
            print('Jest nieparzysta')
    except:
        print('Podano niewłaścuwy znak')

czy_parzysta()