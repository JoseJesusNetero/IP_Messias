def funcao_processamento() :
    
    dist_oasis = float( input("Qual a distancia ate o Oasis ?"))
    
    agua = float( input( "Sua agua no momento ?"))
    
    ##
    
    if  ( agua >= 2 * dist_oasis) :
        
        print("E suficiente")
        
    else  :
        
        print("Nao e suficiente") 
        
    
###################################################

if __name__ == "__main__" :
    
    ##### Inciaindo o programa
    print("--------Iniciando o Programa-------")
    
    ###### chamando a funcao
    funcao_processamento()
    
    ##### terminando o programa
    print("---------Fim do Programa------------")
            