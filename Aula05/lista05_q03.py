def funcao_processamento() :
    
    nome = ""
    
    nome = input( "Diga a especie do seu animal favorito, mamifero ou reptil")
    
    
    #####
    if( nome == "mamifero") :
        
        print("Seu animal e o cachorro ")
        
    else :
        
        print("Seu animal e a tartaruga !")
        
##########################################################

if __name__ == "__main__" :
        
        print("--------Iniciando o Programa-------")
    
        ###### chamando a funcao
        funcao_processamento()
    
        ##### terminando o programa
        print("---------Fim do Programa------------")