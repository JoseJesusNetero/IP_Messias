def funcao_processamento() :
    
    print("Digite o ataque e defesa dos guerreiros, nessa ordem \n")
    
    guerreiro1 = []
    guerreiro2 = []
    
    guerreiro1.append(int(input("Digite seu ataque \n")))
    guerreiro1.append(int(input("Digite sua defesa \n")))
    
    guerreiro2.append(int(input("Digite seu ataque \n")))
    guerreiro2.append(int(input("Digite sua defesa \n")))
    
    ####
    
    if(guerreiro1.sum() > guerreiro2.sum()):
        
        print("Vencedor guerreiro 1 \n")
        
    else:
        
        print("Vencedor guerreiro 2\n")
        
    ####
    
    if( sum(guerreiro1) == sum(guerreiro2)):
        
        print("Vencedor guerreiro 1 )")  if guerreiro1[1] > guerreiro2[1] \
            else  print("Vencedor guerreiro 2 \n")
            
            
            
####################

if __name__ == "__main__" :
    
    ##### Inciaindo o programa
    print("--------Iniciando o Programa-------")
    
    ###### chamando a funcao
    funcao_processamento()
    
    ##### terminando o programa
    print("---------Fim do Programa------------")