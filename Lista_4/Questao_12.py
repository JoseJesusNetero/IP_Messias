def funcao_processamento() :
    

    temperatura = int( input( "Digite a temperatura atual"))

    if( temperatura <= 15) :
        
        print("esta frio \n")
        
    elif ( temperatura <= 25) :
        
        print("esta amenos")
        
    else :
        
        print("Esta muito quente") 
        
###################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")