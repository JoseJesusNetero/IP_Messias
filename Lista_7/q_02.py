def funcao_processamento() :
    
    print("Digite seu numero \n")
    
    numero = int(input('\n'))
    
    i = 0
    
    while( i < 10) :
        
        print( f"{numero} * {i} = { numero * i }\n")
        
        i += 1
        
        
######################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    
    print("Deseja repetir ? 1 para sim, 2 para nao \n")
    
    opcao = input('\n')
    
    if ( opcao == '1') :
        
        funcao_processamento()
        
    
    
    print("---------Fim do Programa----------\n")
        
    