# meu primeiro programa
'''Meu primeiro programa'''
from openpyxl.styles.builtins import total

print("Hello world!")

check1 = 8
check2 = 5.5
print(check1 + check2)

soma = check1 + check2
print(soma)

media = (check1 + check2)/2
print(media)

print(type(check1))
print(type(check2))
print(type(soma))
print(type(media))

nome = "Matheus"
print(type(nome))

# Exercícios

# 1. Faça um programa que exiba seu nome na tela.

nomeCompleto = "Matheus Henrique Marins Vieira\n"
print(nomeCompleto)

# 2. Escreva um programa que exiba o resultado de 2a x 3b, em que a vale 3 e b vale 5.

a = 3
b = 5
soma = (2 * a * 3 * b)
print(soma, "\n")
print()

# 3. Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.

valor1 = 10
valor2 = 12
valor3 =  7
resultado = valor1 + valor2 + valor3
print(resultado, "\n")

# como limitar numeros decimais

print(f"Média = {resultado:.1f}")

d = True
print(type(d))

# Operadores aritméticos
# Operador Operação
#     +      soma
#     -      subtração
#     *      multiplicação
#     /      divisão
#     %      resto da divisão
#     **     potência
#     //     divisão inteira

resto = 10 % 3
print(resto)

inteira = 10 // 3
print(inteira)

# Operadores relacionais (comparação)
# Operador Operação
#   ==     igualdade
#   >      maior que
#   <      menor que
#   !=     diferente
#   >=     maior ou igual
#   <=     menor ou igual

# Operadores lógicos
# Operador      Operação        Exemplo
# not           não             not a
# and           e               (a <= 10) and (c = 5)
# or            ou              (a <= 10) or (c = 5)

# Entrada de dados

check1 = float(input("Checkpoint 1 = "))
check2 = float(input("Checkpoint 2 = "))
media = (check1 + check2)/2
print(f"Média = {media:.1f}")

#Exercícios
# 4. Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

numero1 = float(input("numero 1 = "))
numero2 = float(input("numero 2 = "))
resul = (numero1 + numero2)/2
print(f"Média = {resul:.1f}")

# 5. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
metro = int(input("Digite o valor em Metros = "))
milimetro = metro * 1000
print(f"Média = {milimetro}")

# 6. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Digite o de dias = "))
horas = int(input("Digite o de horas = "))
minutos = int(input("Digite o de minutos = "))
segundos= int(input("Digite o de segundos = "))
segundosTotais = (dias * 24 * 60 * 60) +(horas * 60 * 60) + (minutos * 60) + segundos
#horas = dias * 24
#minutos = horas * 60
#segundos = minutos * 60
print(f"O total de segundos dos dias informados é = {segundosTotais}")

# 7. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do salario = "))
aumento = float(input("Digite o valor do aumento = "))
salarioAumento = salario + (salario * (aumento/100))
print(f"o valor do salario é: {salario}")
print(f"o valor do salario com aumento é: {salarioAumento}")

# 8. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
mercadoria = float(input("Digite o valor da mercadoria: "))
percDesc = float(input("Digite o percentual de desconto: "))
mercadoriaDesc = mercadoria - (mercadoria * (percDesc/100))
print("O valor do desconto é ", percDesc,"%" f" e o valor a se pagar com o desconto e {mercadoriaDesc:.2f}")

# 9. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist = float(input("Digite a distancia a percorrer: "))
velociMedia = float(input("Digite a velocidade media esperada: "))
tempo = dist / velociMedia
print(f"O tempo da viagem será: {tempo:.2f}h")

# 10. Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é F = ((9 x C) / 5) + 32

grauC = float(input("Digite a quantidade de Graus ºC : "))
f = ((9 * grauC) / 5) + 32
print(f"O conversao de graus ºC em ºF é: {f:.1f}")

# 11. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km = int(input("Digite a quantidade de km percorrido: "))
dias = int(input("Digite a quantidade de dias gastos: "))
precoPagar = (km * 0.15) + (dias * 60)
print(f"O valor a ser pago pelos dias e km rodados é {precoPagar:.2f}")

# 12. Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z: z = (x2 + y2) / (x – y)2
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
z = (x ** 2 + y ** 2) / (x - y ) **2
print("O valor de z é: ", z)

# 13. Escreva um programa que receba o salário de um funcionário (float) e retorne o resultado do novo salário com reajuste de 35%.

salarioFunc = float(input("Digite o valor do salario = "))
salarioReajuste = salario + (salario * (35/100))
print(f"o valor do salario com reajuste é: {salarioReajuste}")