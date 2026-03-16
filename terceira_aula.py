# media_final = float(input("Digite a media final: "))
#
# if media_final >= 6:
#     print("Aprovado")
# else:
#     print("Reprovado")
#
# # Exercícios
# # 1. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h.
#
# velocidade = int(input("Digite o valocidade do carro: "))
# if velocidade > 80:
#     multa = (velocidade - 80) * 5
#     print(f"Voce foi multado e o valor da multa é R${multa:.2f}")

# 2. Escreva um programa que leia três números e que imprima o maior e o menor.
# valor1 = float(input("Digite o primeiro numero: "))
# valor2 = float(input("Digite o segundo numero: "))
# valor3 = float(input("Digite o terceiro numero: "))

# if valor1 >= valor2 and valor1 >= valor3:
#     print(f"o primeiro Numero e o maior numero com o valor: {valor1:.2f}")
# if valor2 >= valor1 and valor2 >= valor3:
#     print(f"o segundo Numero e o maior numero com o valor: {valor2:.2f} ")
# if valor3 >= valor1 and valor3 >= valor2:
#     print(f"o terceiro Numero e o maior numero com o valor: {valor3:.2f} ")
# if valor1 <= valor2 and valor1 <= valor3:
#     print(f"o primeiro Numero e o menor numero com o valor: {valor1:.2f}")
# if valor2 <= valor1 and valor2 <= valor3:
#     print(f"o segundo Numero e o menor numero com o valor: {valor2:.2f}")
# if valor3 <= valor1 and valor3 <= valor2:
#     print(f"o terceiro Numero e o menor numero com o valor: {valor3:.2f}")

# maior = valor1
# if valor2 >= valor1 and valor2 >= valor3:
#     maior = valor2
# if valor3 >= valor1 and valor3 >= valor2:
#     maior = valor3
# print(f"Maior = {maior}")
#
# menor = valor1
# if valor2 >= valor1 and valor2 >= valor3:
#     menor = valor2
# if valor3 >= valor1 and valor3 >= valor2:
#     menor = valor3
# print(f"Menor = {menor}")
# 3. Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais, de 15%.

# salario = float(input("Digite o salario do funcionario: "))
# if salario > 1250:
#     aumento = salario * 10/100
#     print(f"O salario do funcionario com aumento é: {aumento:.2f}")
# else:
#     aumento = salario * 15/100
#     print(f"O salario do funcionario com aumento é: {aumento:.2f}")

# 4. Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

# dist = int(input("Digite a distancia a percorrem: "))
# if dist <= 200:
#     passagem = dist * 0.5
#     print(f"O valor da passagem é: {passagem:2.f}")
# else:
#     passagem = dist * 0.45
#     print(f"O valor da passagem é: {passagem:2.f}")

# 5. Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma, subtração, multiplicação e divisão. Exiba o resultado da operação solicitada.

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))
operacao = str(input("Digite a numero da operação desejada entre as opções( soma, subtração, multiplicação e divisão):"))
if operacao == 'soma':
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == 'subtração':
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == 'multiplicação':
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
else:
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")

# 6. Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valorCasa = float(input("Digite o valor da Casa a comprar: "))
salarioComprador = float(input("Digite do seu salario: "))
qtdDeAnos = float(input("Digite a quantidade de anos a pagar: "))
