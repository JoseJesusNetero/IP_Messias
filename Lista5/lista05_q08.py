def funcao_processamento() :
    
    print("informe o seu numero de missoes completadas")
    
    num = int(input())
    
    ##
    
    if( num >= 10 ):
        
        print("Voce receberá 100 moedas !")
        
    elif( num >= 5) :
        
        print("Voce receberá 50 moedas !")
        
    else :
        
        print("Voce recebera 10 moedas")
        
        
#####

if __name__ == "__main__" :
    
    ##### Inciaindo o programa
    print("--------Iniciando o Programa-------")
    
    ###### chamando a funcao
    funcao_processamento()
    
    ##### terminando o programa
    print("---------Fim do Programa------------")