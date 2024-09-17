sua_velocidade = int( input( "Digite agora mesmo a sua velocidade atual "))

if( sua_velocidade <= 80 ):
    
    print( "Muito bem, continue assim ")
    
else :
    
    valor = sua_velocidade - 80 
    
    print( f"Voce vai pagar { 5 * valor }")