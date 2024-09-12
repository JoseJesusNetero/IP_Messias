def funcao_processamento() :
    
    h_extra = int(input("Digite as horas extras \t"))
    
    h_faltou = int( input( "Digite as horas que faltou\t "))
    
    ####
    
    if( h_extra  >  h_faltou +  0.5 *  h_faltou ) :
        
        print("Com bonus")
        
    else:
        
        print("Sem bonus")
        


######################################



if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")
    