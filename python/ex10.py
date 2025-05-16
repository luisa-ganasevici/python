#exercicio1
num = int(input("digite seu numero:"))
if num > 10:
    print("seu numero é maior que dez")
else:
    print("seu numero é menor que dez")  



#exercicio2
print("escreva dois numeros DISTINTOS")
num2 = int(input("digite o numero:"))
num3 = int(input("digite seu numero:"))
if num2 > num3:
    print("o primeiro num é maior q o segundo")
elif num3 > num2:
    print("o segundo numero é maior que o primeiro")
elif num2 == num3:
    print("os dois sao iguais")  


#exercicio6

num4 = int(input("digite seu numero:"))
num5= int(input("digite seu segundo numero"))

if num4 % num5 == 0:
    print("seu numero é divisivel")

else:
    print("Não é divisivel")    
