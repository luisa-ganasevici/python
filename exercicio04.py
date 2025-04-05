
num1 = int(input("digit seu numero: "))
num2 = int(input("digite o segundo numero: "))
num3 = int(input("digite o terceiro numero: "))

if num1 < num2 < num3:
    print(f"a ordem é: {num1},{num2},{num3}")

elif num2 < num1 < num3:
    print(f"a ordem é {num2}, {num1}, {num3}")

elif num2 < num3 < num1:
    print(f"a ordem é {num2}, {num3}, {num1}") 

elif num3 < num2 < num1:
    print(f"a ordem é {num3}, {num2}, {num1}")
    
elif num3 < num1 < num2:
    print(f"a ordem é {num3}, {num1}, {num2}")

elif num1 < num3 < num2:
    print(f"a ordem é {num1}, {num3}, {num2}")