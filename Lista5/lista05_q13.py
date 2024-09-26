def funcao_processamento() :
    
    limite_x = 80
    limite_y = 50
    
    ##
    
    print("Digite a posicao do exercito !\n")
    
    lista = []
    
    lista.append(int(input("Digite o x \n"  )))
    lista.append(int(input("\nDigite o y\n" )))
    
    
    if( lista[0] >= 80 or lista[1] >= 50 ) :
        
        print("Exercito esta fora dos limites !\n")
        
    else:
        
        print("Esta dentro dos limites\n")
        
        
##################

if __name__ == "__main__" :
    
    ##### Inciaindo o programa
    print("--------Iniciando o Programa-------")
    
    ###### chamando a funcao
    funcao_processamento()
    
    ##### terminando o programa
    print("---------Fim do Programa------------")
    
     