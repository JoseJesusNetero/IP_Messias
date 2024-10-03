def funcao_processamento() :
    
    a = ' '
    
    notas = []
    
    cont = 0 
    
    
    while( a != -1 ):
        
        print("Digite as notas ou -1 para encerrar \n")
        
        nota = float(input())
        
        if( nota == -1):
            
            a = -1
        
        notas.append(nota)
        
        cont += 1
        
        
#########

    nota_geral = sum( notas ) / cont
    
    print( f"Sua note e {nota_geral}\n")
        

        
        
#####################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")
        
        
    
    
    
    