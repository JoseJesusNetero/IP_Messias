#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/////////////////

int Funcao_Binario_Para_Decimal ( char p[] , int tam) {

    int i = tam - 1, j;

    int numero_saida = 0;
    ////

    while( i >= 0 )   {

        numero_saida += p[tam] *  pow( 2, i);

        i--;


    }

    ////
    printf( "o Numero em decimal e %d \n", numero_saida);




return 1; }