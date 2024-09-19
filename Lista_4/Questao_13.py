def funcao_processamento() :
    

    print("Informe o seu candidato \n")

    opcao = int( input( "Digite o seu candidato"))

    if( opcao == 1 ) :
        
        print("Seu canditato e o numero 1")
        
    elif( opcao == 2 ) :
        
        print("Seu candidato e o numero 2")
        
    elif( opcao == 3 ) :
        
        print("Seu candidato e o numero 3")
        
    else :
        
        print("Seu candidato e nenhum")
        
#######################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")