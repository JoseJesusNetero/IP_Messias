import random

Lista = []
#####
for i in range(20) :
    
    x = random.randint( 0, 20 )
    Lista.append( x )
    
##########

min = 0
max = 0

#####

for i in range(20) :
    
    if( Lista[i]  < min):
        
        min = Lista[i]
        
    if( Lista[i] > max ):
        
        max = Lista[i]
        
#######

print( max ) 
print( min )