def funcao_processamento() :
    
    moedas_1 = 0
    moedas_050 = 0
    moedas_025 = 0


    print("Digite quantas moedas de cada voce tem \n")
    
    moedas_1   =  (float (input() ))
    moedas_050 =  (float (input() ))
    moedas_025 =  (float (input() ))
    
    #####
    
    Valor_total = 0
    
    Valor_total += moedas_1  +  0.50 * moedas_050 +  0.25 * moedas_025
    
    print(f"O valor total em dinheiro e {Valor_total}")
    







if __name__ == "__main__" :
        
        print("--------Iniciando o Programa-------")
    
        ###### chamando a funcao
        funcao_processamento()
    
        ##### terminando o programa
        print("---------Fim do Programa------------")