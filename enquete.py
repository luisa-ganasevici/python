
def menu() -> int:
    print("sistema enquete")
    print("1 - cadastra pergunta")
    print("2 - visualizar pergunta")
    print("3 - apaga pergunta")
    print("4 - sair")
    return int(input("opcao: "))


#inicio do programa (main)
opcao = 0
while opcao !=4:
    opcao = menu()
    if opcao == 1:
        print("cadastra pergunta")
            def cadastra_pergunta(lista: list):
                num = int(input ("numero: "))
                enun = input("enunciado: ")
                tipo = input("tipo: ")
                alternativas = None 
                if tipo != 'aberta': 

                    #coletar alternativas
                    alternativas =[]
                    i = 1 
                    aux = input(f"alt {i}: ")
                    while aux != "":
                        alternativas.append(aux)
                        i = i + 1
                        aux = input (f"alt {i}: ")

lista.append(num)            
        
    elif opcao == 2:
        print("visualizar pergunta")
    elif opcao == 3:
        print("apaga pergunta")
    elif opcao == 4:
        print("saindo..")
    else:
        print("opcao invalida")

