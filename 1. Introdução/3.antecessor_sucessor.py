# Receba um número inteiro e exiba o número anterior (antecessor) e o próximo (sucessor).
#. Dica: use o operador de subtração e adição com 1.

import os 
os.system("clear")

numero = int(input("Digite um número: "))
print(f"Antecessor {numero - 1}")
print(f"Sucessor {numero + 1}")
