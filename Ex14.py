B = int(input('Quantas balas serão distribuidas? '))
P = int(input('Quantas pessoas tem para dividir? '))
D = int((B/P))
R = (B%P)

print('A quantidade de balas divididas é {} e a o resto {} de balas '.format(D, R))
