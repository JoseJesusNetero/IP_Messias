import random

A = []

lista_aux = []

for i in range(10) :
    
    lista_aux = []
    
    for v in range(10) :
        
        x = random.randint(30, 50)
        lista_aux.append(x)
        
    A.append(lista_aux) 
    
#############################################################################

B = [ [  b * 3  for b in A[ i ][ : ]   ] for i in range(10) ]

print(B)

