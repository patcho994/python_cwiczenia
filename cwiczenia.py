try:
    masa = float(input('Podaj swoja masę: '))
    wzrost = float(input('Podaj swój wzrost: '))
    if masa <= 0 or wzrost <= 0:
        raise Exception('Masa i wzrost nie mogą być mniejsze od 1')
    
    bmi = masa / (wzrost * wzrost)
    komunikat = ''
    if bmi < 18.5:
        komunikat = 'Niedowaga'
    elif bmi >= 18.5 and bmi < 24.9:
        komunikat = 'Prawidłowa masa ciała'
    elif bmi >= 24.9 and bmi < 30:
        komunikat = 'Nadwaga'
    else:
        komunikat = 'Otyłość'
        
    print(f'Twoje BMI wynosi {bmi}. Komunikat: {komunikat}')
        
except ValueError: 
    print('Podano nieprawidłową wartość')
except Exception as error:
    print(error)

