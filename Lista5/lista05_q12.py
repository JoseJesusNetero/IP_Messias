def funcao_processamento() :
    
    espada = []
    lanca  = []
    arco   = []
    
    ##
    
    print("Digite o ataque e defesa de cada uma destas armas \n Espada\
            \n Lanca \nArco")
    
    ##
    
    for i in range(2) :
        
        print("Espada\n")
        
        espada[i] = int(input())

    
    for i in range(2) :
        
        print("Lanca\n")
        lanca[i] = int(input())  
        
        
    for i in range(2) :
        
        print("Arco\n")
        arco[i] = int(input())      
    
    
    ####
    
    if( espada[0] < 50 or lanca[0] < 50 or arco[0] < 50):
        
        print("Escolha outra arma \n")
        
    if( espada[1] < 70 or lanca[1] < 70 or arco[1] < 70): 
           
        print("Escolha outra arma \n")
    
    if ( espada[0] >= 50  and  espada[1] >=  70 ):
        
        print("espada passou !\n")
        
    
    if ( lanca[0] >= 50  and  lanca[1] >=  70) :
        
        print("lanca passou !\n")
        
        
    if( arco[0] >= 50  and  arco[1]  >=  70) :
        
        print("arco passou\n")
#####################