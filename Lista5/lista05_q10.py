def funcao_processamento() :
    
    print("Escolha a porta desejada  ou digite -1 para sair\n")
    
    while True:
    
        porta = int(input())
        
        match porta :
            
            case 1:
                
                print("Voce fara desafio 1 ! \n")
                
            case 2:
                
                print("Voce fara desafio 2 ! \n")
                
            case 3:
                
                print("Voce fara desafio 3 ! \n")
                
            case 4:
                
                print("Voce fará desafio 4 ! \n")
                
            case 5:
                
                print("Voce fará desafio 5 ! \n")                
    

            case _:
            
                break
                
#################

if __name__ == "__main__" :
    
    ##### Inciaindo o programa
    print("--------Iniciando o Programa-------")
    
    ###### chamando a funcao
    funcao_processamento()
    
    ##### terminando o programa
    print("---------Fim do Programa------------")