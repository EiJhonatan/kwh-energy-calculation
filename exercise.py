kwh = float(input('Quantos kwh?'))
tipo = input('Qual o tipo da instalacao?(R, C, I)')

if (tipo =='R'):
    if kwh >= 500:
        preco = 0.65
    else:
        preco = 0.4
    print(f'Tatal a pagar: {kwh * preco}')
elif (tipo =='C'):
    if kwh >= 1000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'Tatal a pagar: {kwh * preco}')

elif (tipo =='I'):
    if kwh >= 5000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'Tatal a pagar: {kwh * preco}')
else:
    print('Instalacao Invalida. Encerrando...')