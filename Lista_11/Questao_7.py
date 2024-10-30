import random

Vetor_A = []
Vetor_B = []

for i in range( 10 ) :
    
    a = random.randint( 90, 100 )
    b = random.randint( 90, 100 )
    Vetor_A.append(a)
    Vetor_B.append(b)
    #############
    
###############################


Ocorrencias = []

for i in range(10) :
    
    if( Vetor_A[i] == Vetor_B[i]):
        
        Ocorrencias.append( [Vetor_A[i] , i ])
        
    
#######

print( Ocorrencias )
    