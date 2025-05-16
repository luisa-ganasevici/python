#exercicio 7
numero = int(input("Digite um número inteiro entre 0 e 99: "))

if 0 <= numero <= 99:
    dezenas = numero // 10
    unidades = numero % 10

    print("Dígito das dezenas:", dezenas)
    print("Dígito das unidades:", unidades)
else:
    print("Número fora do intervalo permitido (0 a 99).")



#exercicio 8

x = int(input("Digite o número de camisas: "))
y = int(input("Digite o número de calças: "))
z = int(input("Digite o número de pares de sapato: "))

combinacoes = x * y * z

print("O número total de maneiras diferentes de se vestir é:"
      , combinacoes)

#exercicio 9
prod = float(input("digite o preço:"))
desconto = int(input("digite o desconto:"))
descontoF = prod * desconto / 100
precoF = prod - descontoF
print("com essa porcentgem de desconto, vc pagará:", precoF)
aumento = descontoF + prod
print("se for aumentado, sera aumentado:", aumento)