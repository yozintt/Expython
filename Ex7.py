TG = float(input('Qual o tempo gasto na viagem? (ex: 1.30, uma hora e meia) '))
VM = int(input('Qual a velocidade média feita na viagem? (ex: 80, oitenta km/h) '))
D = (TG * VM)
print('tempo gasto: {:.2f}'.format(TG))
print('Velocidade média: {}'.format(VM))
print('A distância percorrida é: {:.2f}  '.format(D))

LU = (D / 12)

print('Quantidade de litros gasta na viagem é: {:.2f} '.format(LU))