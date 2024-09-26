arquivo = open("vingadores.txt", 'r')

lista = arquivo.readlines()

for i in lista:
    
    print(f"Venha para minha festa {i} ! \n")