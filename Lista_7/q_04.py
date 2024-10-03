import random


def funcao_processamento() :
    
    numero = random.randint(1 , 100)
    
    palpite = 0
    
    while(palpite != numero) :

        print("Digite seu palpite \n")  
              
        palpite = int(input())
        
        if palpite == numero :
            
            print("Voce acertou !")
            
        else :
            
            print("tente de novo \n")
            
            
#######################

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")