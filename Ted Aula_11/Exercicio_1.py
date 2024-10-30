import random

import random

Lista = []
Ocorrencias = []
#####
for i in range(10) :
    
    x = random.randint( 0, 2 )
    Lista.append( x )
    
##########

for i in range(10) :
    
    v = i + 1
    
    for v in range( v , 10) :
        
        if( Lista[ i ] == Lista[ v ]) :
            
            Ocorrencias.append( [i, v])
            
#########
print(Ocorrencias)
            
            
