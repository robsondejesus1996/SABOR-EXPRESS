idade = int(input('Informe sua idade :'))


if idade >= 0 and idade <=12:
    print('Criança')
elif idade >=13 and idade <=18:
    print('Adolescente')
else:
    print('Adulto')             