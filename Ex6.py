VHA = float(input('Qual o valor da hora/aula? '))
HSM = int(input('Número de horas trabalhadas? '))
INSS = float(input('Digite o desconto do INSS: '))

SB = (VHA * HSM)
print('O seu salário bruto é: {}'.format(SB))

SL = SB - (SB * (INSS/100))
print('O seu salário liquido é: {:.2f}'.format(SL))