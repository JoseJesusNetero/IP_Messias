def funcao_processamento() :
    
    esq = 1000
    dir = 2000
    
    i = esq
    ###
    
    achados = 0
    
    while( i < 2000) :
        
        if( i % 11 == 5) :
            
            achados += 1
        
        ####
        i += 1
        
    ###
    
    print(f"Foram achados {achados} numeros")
    
####################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")