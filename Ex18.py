

CanA = int(input('Quantos votos o candidato A possui? ')) 
CanB = int(input('Quantos votos o candidato B possui? '))
CanC = int(input('Quantos votos o candidato C possui? '))
VTnulo = int(input('Quantos votos nulos na eleição? '))
VTbranco = int(input('Quantos votos em branco na eleição? '))

#Votos elegiveis em candidatos:
VTC = (CanA + CanB + CanC)

#Eleitores:
E = (VTC + VTnulo + VTbranco)

#Percentual do candidato A:
PA = (CanA * (100/E))
#Percentual do candidato B:
PB = (CanB * (100/E))
#Percentual do candidato C:
PC = (CanC * (100/E))

#Percentual de Votos em Branco:
PVB = (VTbranco * (100/E))
#Percentual de votos nulos:
PVN = (VTnulo * (100/E))

print('Número total de eleitores foi de : {}'.format(E))
print('percentual de votos elegiveis ao candidato A: {:.2f} '.format(PA))
print('percentual de votos elegiveis ao candidato B: {:.2f} '.format(PB))
print('percentual de votos elegiveis ao candidato C: {:.2f} '.format(PC))
print('Percentual de votos nulos pelos eleitores: {:.2f}'.format(PVN))
print('Percentual de votos em branco pelos eleitores: {:.2f}'.format(PVB))