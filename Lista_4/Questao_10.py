def funcao_processamento() :
    
    print("Comece digitando os lados")
    
    ladoa = float( input( "Primeiro lado:\t"))
    ladob = float( input( "Segundo lado:\t"))
    ladoc = float( input( "Terceiro lado:\t"))

######

    if( ladoa == ladob) :
        
        if( ladob == ladoc ):
            
            print("Equilatero")
            
            
        else:
            
            print("Isosceles")
            
######

    elif( ladoa == ladoc ) :
        
        
        if( ladob == ladoc ) :
            
            print("Equilatero")
            
        
        else :
            
            print("Isosceles")
            

    elif( ladob == ladoc) :
        
        print("Isosceles")






if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")
    










