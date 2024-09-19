def funcao_processamento() :

    print("Digite um numero")

    numero = int( input( "Qual o numero : \t"))
    ######

    if( numero > 50 ) :
        
        print( "E maior que 50 ")
        
    elif ( numero < 50 ) :
        
        print("E menor que 50")
        
    else :
        
        print("E igual")
        
###################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")