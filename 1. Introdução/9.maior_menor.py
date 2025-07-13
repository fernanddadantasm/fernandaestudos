import os 
os.system("clear")


numero_um = int(input("Diigte um número: "))
numero_dois = int(input("Digite outro número: "))

if numero_um > numero_dois:
    print("O primeiro número digitado é o maior!") 
elif numero_dois > numero_um:
    print("O segundo número digitado é o maior!")

elif numero_um == numero_dois:
    print("Os números digitados são iguais!")
