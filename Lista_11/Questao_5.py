import random

Vetor_A = []
Vetor_B = []

#######

for i in range( 10 ) :
    
    a = random.randint( 0, 20 )
    b = random.randint( 90, 100 )
    Vetor_A.append(a)
    Vetor_B.append(b)
    #############
    
###############################

Vetor_C = [ a + b for a,b in zip(Vetor_A, Vetor_B) ]

#######

print(Vetor_C)