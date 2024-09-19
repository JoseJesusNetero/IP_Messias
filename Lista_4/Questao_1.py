def funcao_processamento() :

    Nota_1 = float( input ("Qual foi sua primeira nota ?"))

    Nota_2 = float( input ("Qual foi sua segunda nota ?"))

    Media = ( Nota_1 + Nota_2 ) / 2

    ######

    if( Media >= 6.0 ) :
        
        print("Voce foi aprovado \n")
        
    else :
        
        print("Boa sorte na proxima\n")
        
        
    
######################################################
if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")