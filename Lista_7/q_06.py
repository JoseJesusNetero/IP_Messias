def funcao_processamento() :
    
    print("Digite qual numero deseja  \n")
    
    N = int(input())
    
    aux = 2
    
    while ( aux <=  N / 2) :
        
        if( N % aux == 0 ) :
            
            print("Numero nao e primo")
            break
        
        aux += 1
            
    print("Numero e primo \n")
    
###############################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")    