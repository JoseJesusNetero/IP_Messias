import random

Lista = []

for i in range(20):
    
    x = random.randint(100, 105)
    Lista.append(x)
    
###############

x = 101

i = 0

for i in range(20):
    
    if(( x == Lista[i] )):

        Lista.remove(x)
        
#######
print(Lista)