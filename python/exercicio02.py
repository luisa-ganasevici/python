num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
opr = input("escolha um operador (+-*/): ") 


if opr == "+":
    resultado = num1 + num2

if opr == "-":
    resultado = num1 - num2

if opr == "*":
    resultado = num1 * num2

if opr == "/":
    resultado = num1 / num2

print (f"{resultado}")