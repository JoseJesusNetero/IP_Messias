def funcao_processamento() :
    

    print("Digite um numero \n")

    numero_1 = int( input ("\n"))

    print("Digite outro numero \n")

    numero_2 = int( input ("\n"))

    if( numero_1 > numero_2 ) :
        
        print( f" {numero_2} \t {numero_1}")
        
    else :
        
        print( f" {numero_1} \t {numero_2}")
        
####################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")
    