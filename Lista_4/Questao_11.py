def funcao_processamento() :
    

    sua_idade = int( input("Digite sua idade "))

    if( sua_idade >= 12 and sua_idade <= 60  ) :
        
        print("Seu preco e 25 reais")
        
    else :
        
        print("Seu preco e 15 reais")    
        
#########################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")