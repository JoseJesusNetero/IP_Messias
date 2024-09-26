def media( valor_a, valor_b, valor_c ) :
    
    return ( ( float(valor_a + valor_b + valor_c / 2)))

##############

def funcao_processamento () :
    
    print( "Qual as notas dos primeiro candidato ? \n")
    
    candidato_a = []
    
    for i in range(3) :
        
        print(f"Nota {i + 1} \n")
        
        nota = float(input())
        
        candidato_a.append(nota)
        
    ###
    
    print( "\nQual as notas dos segundo candidato ? \n")
    

    candidato_b = []
    
    for i in range(3) :
        
        print(f"Nota {i + 1} \n")
        
        nota = float(input())
        
        candidato_b.append(nota)
        

    print( "\nQual as notas dos terceiro candidato ? \n")
    
    candidato_c = []
    
    for i in range(3) :
        
        print(f"Nota {i + 1} \n")
        
        nota = float(input())
        
        candidato_c.append(nota)
        
        
    ###################
    
    Media_a = media( candidato_a[0], candidato_a[1], candidato_a[2])
    
    Media_b = media( candidato_b[0], candidato_b[1], candidato_b[2])
    
    Media_c = media( candidato_c[0], candidato_c[1], candidato_c[2])
    
    ###################
    
    if( Media_a == Media_b  or  Media_a == Media_c or Media_b == Media_c):
        
        print("Houve empate \n")
        
    ###############
    
    if Media_a > Media_b and Media_a > Media_c:
        
        print("Candidato_a \n")
        
    elif Media_b > Media_a and Media_b > Media_c:
        
        print("Candidato b\n")
        
    elif Media_c > Media_b and Media_c > Media_a:
        
        print("Candidato c\n")
        


###########################################

if __name__ == "__main__" :
    
    ##### Inciaindo o programa
    print("--------Iniciando o Programa-------")
    
    ###### chamando a funcao
    funcao_processamento()
    
    ##### terminando o programa
    print("---------Fim do Programa------------")