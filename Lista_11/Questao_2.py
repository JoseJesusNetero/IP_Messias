print("Digite as notas de cada um dos 5 alunos")

numero = 5
Notas = []

for i in range( 5 ) :
    
    for v in range( 3 ) :
        
        print(f"Digite a {v + 1} do aluno {i + 1}")
        Nota = float(input())
        Notas.append(Nota)
        
#############

media = [ (sum(Notas[ i : i + 3 ]) / 3) for  i  in range(0, 15, 3 )   ]


###########################################

print("A media de cada um e a seguinte lista ")

print(media)
    
#############

print("A quantidade de alnos que obtiveram nota acima da media e : \n ")

#####
for i in range(5) :
    

    print( media [i] )  if  media[i] >  7  else  print(" ") 

#####
print(f"E a media geral da turma e {sum(media) / 5} ")