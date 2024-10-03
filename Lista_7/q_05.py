def funcao_processamento() :
    
    print("Digite até que termo quer a sequencia ? \n")
    
    N = int(input())
    
    a = 0
    b = 1
    aux = 0
    
    ##
    while( aux <= N) :
        
        aux += 1
        
        temp = a + b
        
        print(f" { a } \n { b }  \n")
        
        a = b
        
        b = temp
        
        
    
    
##############################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")