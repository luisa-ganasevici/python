print("exemplos")

minhaLista = []
minhaLista.append("item1")
minhaLista.append("item2")

print(minhaLista)

print("numeros")

meusNum = [1,4,9,0]
meusNum.append(7)

print(meusNum)

print("substituir elementos")

frutas = ["uva", "kiwi", "maçã", "abacate"]

print(frutas[2])
frutas[2] = "melancia"
print(frutas)

print("remover elemento da lista")
remove = frutas.pop(1)
print(frutas)

print("concatenando listas")

individual = [" natacao "," tenis "," judo "]
coletivo = [" futebol "," volei "," basquete "]
esporte = individual + coletivo
print ( esporte )

outros = (" Boxe "," Golfe ")


for esp in outros :
    individual.append (esp)
print (individual)


