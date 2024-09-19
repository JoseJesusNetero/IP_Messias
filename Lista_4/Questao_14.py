def funcao_processamento() :
    

    salario_mensal = float( input ("Digite sua renda mensal "))

    if( salario_mensal <= 2000.00) :
        
        print("Esta livre, isento ")
        
    elif( salario_mensal <= 3500 ) :
        
        print(f"Voce vai pagar { 0.10 * salario_mensal} pro Leao ! ")
        
    else:
        
        print(f"Vai pagar {0.15 * salario_mensal} ")
        
#################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")