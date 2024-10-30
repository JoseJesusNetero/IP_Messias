import random

Vetor_A = []

for i in range( 10 ) :
    
    b = random.randint( 90, 100 )
    Vetor_A.append(b)
    #############
    
###############################
x = 5

Vetor_M = [ x * i for i in Vetor_A ]

#######

print(Vetor_M)
