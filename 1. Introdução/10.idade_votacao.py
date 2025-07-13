import os 
os.system("clear")

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não tem idade para votar!")
elif idade >= 16:
    print("Liberado para votar!")
elif idade == 18 or idade ==60:  
    print("Voto obrigatório!")