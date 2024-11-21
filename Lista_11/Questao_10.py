import random

A = []

lista_aux = []

for i in range(10) :
    
    lista_aux = []
    
    for v in range(10) :
        
        x = random.randint(100, 150)
        lista_aux.append(x)
        
    A.append(lista_aux) 
    
#######

x = 0

for i in range(5) :
    
    for v in range(5) :
        
        if( x == A[i][v]) :
            
            print("Existe")
            break