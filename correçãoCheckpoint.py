cp1 = float(input("Digite o valor do primeiro checkPoint: "))
cp2 = float(input("Digite o valor do segundo checkPoint: "))
cp3 = float(input("Digite o valor do terceiro checkPoint: "))
sprint1 = float(input("Digite o valor da primeiro sprint: "))
sprint2 = float(input("Digite o valor da primeiro sprint: "))
GlobalSolution = float(input("Digite o valor da Global Solution: "))

menorCp = cp1
if cp2 <= cp1 and cp2 <= cp3:
 menorCp = cp2
if cp3 <= cp2 and cp3 <= cp1:
 menorCp = cp3

print(f"O menor valor é {menorCp}.")

media = ((cp1 + cp2 + cp3 - menorCp + sprint1 + sprint2) / 4) * 0.4 + GlobalSolution * 0.6
media_peso = media * 0.4


print(f"A media do aluno(a) é: {media:.1f} ")
print(f"A media do aluno(a) com o peso do semestre é: {media_peso:.1f} ")