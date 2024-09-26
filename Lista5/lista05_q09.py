def funcao_processamento() :
    
    opcao = print( input("Digite a opcao 1, Feitico 1, 2_ Feitico 2, Feitico_3 \n"))
    
    opcao = int(input())
    
    ####
    
    match opcao:
        
        case 1:
            
            print("1")
         
        case 2:
            
            print("2")
            
        case 3:
            
            print("3")   
            
#######
        
if __name__ == "__main__" :
    
    ##### Inciaindo o programa
    print("--------Iniciando o Programa-------")
    
    ###### chamando a funcao
    funcao_processamento()
    
    ##### terminando o programa
    print("---------Fim do Programa------------")
    