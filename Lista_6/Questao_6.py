def funcao_processamento() :
    
    lista = ["Charles Chaplin", \
             "Steve Wonder", "Sarah Conor", "Blade", "Liu Kang"]
    
    print("Os convidados da festa sao")
    ###
    
    for i in lista: 
        
        print(f"{i}\n")
        
    ####
    
        print("Sejam todos bem vindos e acomodados\n")
        ###
        
        for i in lista:
            
            print(f"Bem vindo(a) {i}\n")
            
    
    print("o ultimo e o penultimo da lista desistiram\n")
    
    print(f"Os faltantes foram {lista[3]}  e {lista[4]} \n")
    
    lista.pop()
    lista.pop()

    print("Agora restaram\n")
    
    for i in lista :
        
        print(f"{i}\n")
              
##Adicionar á lista     

### append
### extend  


        
#####################################################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")