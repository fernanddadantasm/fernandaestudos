# Peça ao usuário dois números (inteiros ou decimais) e exiba a soma,
#  subtração, multiplicação e divisão entre eles. 
# Use os operadores +, -, *, /. Exiba os resultados com mensagens explicativas.

import os
os.system("clear")

numero_um = int(input("Digite um número: "))
numero_dois = int(input("Digite um segundo número: "))
os.system("clear")
print("=== RESULTADOS === ")
print(f"Soma {numero_um + numero_dois} ")
print(f"Subtração {numero_um - numero_dois} ")
print(f"Multplicação {numero_um * numero_dois} ")
print(f"Divisão {numero_um / numero_dois} ")

