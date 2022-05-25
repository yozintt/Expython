
    #Horario do cliente: 
HDC = str(input('Qual é o tempo ? (no formato 00:00:00) '))
HDC = HDC.split(':')

    #Definindo as colunas Hr:Min:Seg
hora = int(HDC[0])
minuto = int(HDC[1])
segundo = int(HDC[2])

    #Calculo de conversão de Hr para segs:
CVSG = hora*3600+minuto*60+segundo
    #Resposta na tela
print('O seu tempo convertido é: {} segundos'.format(CVSG))