
py = 3.14159
r = float(input('Qual o valor do raio? '))
H = float(input('Digite o valor da altura: '))
CT = 50.00
ArT = 3
VT = 5

# Cálculo da Area:
Area = 2 * py * r * (H + r)

# Cáculo de quantas latas:
QL = int(Area//ArT)

# Cálculo do valor:
CV = CT * QL

print('A area do cilindro é igual a: {:.2f} uma lata de de tinta custa {:.2f}, você irá precisar de {} latas, então o seu custo será {:.2f} '.format(Area, CT, QL, CV ))
