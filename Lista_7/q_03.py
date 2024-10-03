def funcao_processamento() :
    
    frase = input("Digite a frase que deseja ")
    
    vogais = ['a', 'e', 'i', 'o','u' ]
    
    ###
    
    cont_vogal = 0
    cont_consoante = 0
    
    ###
    
    for i in frase:
        
        if i in vogais:
            
            cont_vogal += 1
            
        else :
            
            cont_consoante += 1
            
###

    print(f"Sao tantas {cont_vogal} vogais e {cont_consoante} consoantes \n ")
    
#################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")
    
    #####