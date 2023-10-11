peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
imc = peso / (altura ** 2)

print("Seu IMC é:", imc)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Seu peso está dentro da faixa normal.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
elif imc < 34.9:
    print("Você está com obesidade grau I.")
elif imc < 39.9:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade grau III (obesidade mórbida).")
