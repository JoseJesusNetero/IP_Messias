Valor = float( input( "Digite quanto você gastou "))

desconto = 0.0

if( Valor > 100.00 ) :
    
    desconto = 0.1 * Valor
    
    Valor -= desconto
    
elif( Valor >= 50.00 )    :
    
    desconto =   0.05 * Valor
    
    Valor -= desconto 
    

    
print( f"O valor e { Valor } e o desconto e {desconto}")