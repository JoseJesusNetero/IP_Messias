import random

Vetor_A = []
####
for i in range( 30) :
    
    a = random.randint( 90, 100 )
    Vetor_A.append(a)
    #############
    
###############################

Ocorrencias = 0

x = 95

for i in range(30) :
    
    if( Vetor_A[i] == x ):
        
        Ocorrencias += 1
        
#######
print( Ocorrencias )
    