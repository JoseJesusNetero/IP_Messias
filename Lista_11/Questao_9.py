import random

A = []

a = 5
b = 10

lista_aux = []

for i in range(5) :
    
    lista_aux = []
    
    for v in range(5) :
        
        x = random.randint(a * v, b * v)
        lista_aux.append(x)
        
    A.append(lista_aux) 
    
#######

x = 13

for i in range(5) :
    
    for v in range(5) :
        
        if( x == A[i][v]) :
            
            print("Existe")
            break