import os 
os.system("clear")

temperatura = int(input("Digite a temperatura em Celcius:  "))

conversão = (temperatura * 1.8) + 32

print(f"A temperatura digitada em Fahrenheit é: {conversão}")