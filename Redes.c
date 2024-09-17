#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main()        {

    srand( time ( NULL ));

    //////

    int ip_Rede[12] = {1, 9, 2, 1, 6, 8, 0, 0, 1, 0, 0, 0 };

    int mask[12]    = {2, 5, 5, 2, 5, 5, 2, 5, 5, 0, 0, 0};
    
    int ip_s[12]     = {1, 9, 2, 1, 6, 8, 0, 0, 1, 0, 0, 0 };

    //////

    int i, j;
    
    for( i = 9; i < 12; i++)    

        ip_Rede[i] = ( rand() % 10) ;


    for( i = 0; i < 12; i++)
    printf( "%d" , ip_Rede[i]);


////// 
/// Supondo que sao 24 bits de rede, entao para o host sobram 8 numeros









    return 1;
}