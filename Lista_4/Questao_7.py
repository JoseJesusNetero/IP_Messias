quant_atual =  int( input( "Digite a quantidade atual em estoque "))

quant_max   =  int( input( "Digite a quantidade max em estoque  "))

quant_min   =  int( input( "Digite a quantidade minima em estoque "))

######################

quant_media = (quant_max + quant_min) / 2

#####################################

if quant_atual >= quant_media :
    
    print( "Nao efetuar compra")
    
else :
    
    print( "Efetuar compra") 