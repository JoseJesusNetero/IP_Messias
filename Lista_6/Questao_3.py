def funcao_processamento() :
    
    print("Digite o seu numero desejado\n")
    
    numero = int(input())
    
    ####
    j = 1
    
    while( j <= 10) :
        
        print(f"{numero * j}\n")
        
        j += 1
    ###
    
##############################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")