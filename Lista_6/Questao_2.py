def funcao_processamento() :
    
    i = 1
    
    
    while( i <= 10) :
        
        
        j = 1
        print(f"{i * (i + 1)}")

        while ( j <= 9 ):
            
            print(f" {i * j}\n")
            
            j += 1
    
        i += 1
        
########################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")