Sal = float(input('Digite o seu salário: '))
Per = float(input('Digite o percentual do reajuste: '))
Nsal = (Sal +  (Sal * (Per/100)))
print('O novo salário é: {:.2f}'.format(Nsal))
