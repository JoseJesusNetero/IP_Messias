def funcao_processamento() :
    

    print("Digite sua conta \n")

    conta = int(input())

    print("Digite seu debito \n")

    debito = float(input())

    print("Digite seu credito \n")

    credito = float(input())

    print("Digite seu saldo \n")

    saldo = float(input())

    ##

    saldo = saldo - debito

    saldo += credito

    ##

    if( saldo >= 0) :
        
        print("saldo positivo")
        
    else :
        
        print('saldo negativo')

############################################3

if __name__ == "__main__" :
    
    print("---------Inicio do Programa----------\n")
    
    funcao_processamento()
    
    print("---------Fim do Programa----------\n")


