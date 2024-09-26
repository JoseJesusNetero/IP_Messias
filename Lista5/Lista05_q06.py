def funcao_processamento() :
    
    Primeiro_Dragao_v = float(input("Qual a velocidade deste ?"))
    
    Segundo_Dragao_v = float(input("E agora qual a velocidade deste ?"))
    
    ######
    
    Primeiro_Dragao_t = float(input("E qual o tempo do primeiro?"))
    
    Segundo_Dragao_t =  float(input("E qual o tempo do segundo?"))
    
    
    Vencedor = "Primeiro_Dragao"  \
        if (Primeiro_Dragao_v/Primeiro_Dragao_t)  > \
            (Segundo_Dragao_v/Segundo_Dragao_t)  else\
                "Segundo_Dragao"
    #####
    
    print(f"O mais rapido e { Vencedor }")
    

###############################################

if __name__ == "__main__" :
    
    ##### Inciaindo o programa
    print("--------Iniciando o Programa-------")
    
    ###### chamando a funcao
    funcao_processamento()
    
    ##### terminando o programa
    print("---------Fim do Programa------------")
        