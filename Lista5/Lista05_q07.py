def funcao_processamento() :
    
    print("Informe a altura da planta \n")
    
    planta = float( input())
    
    ####
    
    if( planta < 1.0 ):
        
        print("pequena")
        
    elif( planta < 3.0) :
        
        print("media")
        
    else :
        
        print("grande")
        
        
        
#####

if __name__ == "__main__" :
    
    ##### Inciaindo o programa
    print("--------Iniciando o Programa-------")
    
    ###### chamando a funcao
    funcao_processamento()
    
    ##### terminando o programa
    print("---------Fim do Programa------------")