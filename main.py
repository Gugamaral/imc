nome = input('Informe seu nome: ')
peso = str(input('Informe seu peso em kg: '))
altura = str(input('Informe sua altura em metros:'))

peso = peso.replace(',', '.')
altura = altura.replace(',', '.')

try:
    peso = float(peso)
    altura = (float)(altura)

    imc = peso/ (altura**2)

    print(f'O valor do IMC de {nome} é {imc:,.2f}.')

    if imc <17:
        print(f'{nome} está muito abaixo do peso.')
    elif imc < 18.5:
        print(f'{nome} está abaixo do peso.')
    elif imc <25:
        print(f'{nome} está no seu peso ideal')
    elif imc <30:
        print(f'{nome} está levemente acima do peso  ')
    elif imc <35:
        print(f'{nome} está com obesidade grau I  ')
    elif imc <40:
        print(f'{nome} está com obesidade grau II  ')
    else: 
        print(f'{nome} está com obesidade grau III Mórbida')

except:
    print('Não foi possível calcular o IMC.')
