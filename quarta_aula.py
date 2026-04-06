# x = 0

# while x <= 3:
#     print(x)
#     x = (x + 1)

# Exercícios
# 1. Faça um programa para exibir os números de 1 a 100.

# numero = 1
#
# while numero <= 100:
#     print(numero)
#     numero = numero + 1
# print()

# 2. Faça um programa para exibir os números de 50 a 100.

# numeros = 50
#
# while numeros <= 100:
#     print(numeros)
#     numeros = numeros + 1
#
# print()

# 3. Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! Na tela.

# from time import sleep
#
# contagem = 10
#
# while contagem >= 0:
#     print(contagem)
#     sleep(1)
#     contagem = contagem - 1

# print('Fogo')

# 4. Faça um programa para imprimir de 1 até o número digitado pelo usuário que mostre apenas os números ímpares.

# valor = int(input("Digite um valor :"))
# cont = 1
#
# while cont <= valor:
#     print(cont)
#     cont += 1


# 5. Faça um programa para escrever os 10 primeiros múltiplos de 3.

# x = 3
# while x <= 30:
#     print(x)
#     x = x + 3
#
# # 6. Faça um programa para exibir os resultados de uma tabuada no formato: 2 x 1 = 2, 2 x 2 = 4, ...
#
# num = int(input("Tabuada de:"))
# var= 0
#
# while x <= 10:
#     print(f"{num} X {x}  = {num * x}")
#     x += 1

# 7. Modifique o programa interior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

# num = int(input("inicio da Tabuada de:"))
# x = 0
# var= int(input("fim da tabua de:"))
#
# while x <= var:
#     print(f"{num} X {x}  = {num * x}")
#     x += 1

# 8. Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total do ganho com juros no período.

# deposito = float(input("Digite o valor depositado:"))
# juros = float(input("Digite a taxa de juros: "))
# mes = 1
# ganho = 0
# while mes <= 24:
#     print("mes = ",  + mes)
#     print(f"o valor do depois com o juros do mes é: {deposito:.2f}")
#     print(f"o valor do juros do mes é: {ganho:.2f}")
#     print()
#     jurosganho = deposito * (juros/100)
#     deposito = deposito + jurosganho
#     ganho = ganho + jurosganho
#
#     mes += 1

# 9. Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês e você deve considerá-lo para o cálculo de juros do mês seguinte.

deposito = float(input("Digite o valor depositado inicialmente:"))
juros = float(input("Digite a taxa de juros: "))
depmes = float(input("Digite o valor depositado mensalmente: "))
mes = 1
ganho = 0
while mes <= 24:
    print("mes = ",  + mes)
    jurosganho = deposito * (juros / 100)
    ganho = ganho + jurosganho
    print(f"o valor do juros do mes é: {ganho:.2f}")
    print(f"o valor depositado esse mes é: {depmes:.2f}")
    deposito = deposito + depmes + jurosganho
    print(f"o valor do deposito com o juros do mes é: {deposito:.2f}")
    print()

    mes += 1



