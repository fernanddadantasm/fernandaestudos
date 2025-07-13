# Peça ao usuário duas notas (números com casas decimais) e calcule a média. 
#  Depois, exiba a média com uma mensagem que diga se o aluno está aprovado (média >= 6)

import os 
os.system("clear")

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
media = (nota_um + nota_dois) / 2

if media >= 6:
    print(f"Aprovado!")
    print(f"Média : {media:.2f}")
else: 
    print(f"Reprovado!")
    print(f"Média:{media:.2f} ")