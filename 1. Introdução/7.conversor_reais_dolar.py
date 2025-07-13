import os 
os.system("clear")

valor = float(input("Digite um valor em R$: "))
cotacao_dolar = float (input("Digite a cotação atual do dolar (Quanto ele está valendo no dia atual): "))

total = valor * cotacao_dolar
print(f"Com R${valor:.2f}, você teria aproximadamente US${total:.2f}")

