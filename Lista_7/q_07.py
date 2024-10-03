def funcao_processamento() :
    
    N = int(input("Digite o numero para se calcular fatorial desejado \n"))
    
    aux = N - 1
    
    result = N
    
    while( aux > 0) :
        
        result *= aux
        
        aux -= 1
    
    
    print(f" { result } \n")
##################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")

