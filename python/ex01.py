print("coloque qntos valores desejar pra soma-los,qndo acabar digite 0")
num = int(input("Digite um inteiro: "))
soma = 0

while num != 0:
        soma = soma + num
        num = int(input("Digite um inteiro: "))

print("A soma é", soma)