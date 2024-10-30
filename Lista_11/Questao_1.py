print("Digite 5 nomes de clubes ")

Lista = []

for i in range(5) :
    
    Nome = input("")
    Lista.append(Nome)

    
#####################

print("Agora diga um nome para verificar se ele pertence a lista")

Nome = input("")

####

aux = 5

while( (Nome != Lista[aux - 1] ) and ( aux > 0 ) ) :
    
    aux -= 1
    
###

if ( aux <= 0 ):
    
    print("Nao achei")
    
else :
    
    print("Achei")


