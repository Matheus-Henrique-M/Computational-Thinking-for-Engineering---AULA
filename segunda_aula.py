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
