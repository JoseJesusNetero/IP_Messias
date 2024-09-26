def funcao_processamento() :
    
    ferro = float(input( "Digite a qtde ferro "))
    
    ouro = float( input( "Digite a qtde ouro "))
    ####
    
    peso_total = ferro + ouro
    
    ####
    
    if ( ferro <  0.7 * peso_total):
        
        print("Atualize os pesos ! , quantidade de ferro insuficiente")
      
      
        
    #########################################################
    
    if __name__ == "__main__" :
        
        print("--------Iniciando o Programa-------")
    
        ###### chamando a funcao
        funcao_processamento()
    
        ##### terminando o programa
        print("---------Fim do Programa------------")