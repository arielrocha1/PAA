#include<stdio.h> 
  
    /* Função apenas para retornar o numero maior */
int max(int a, int b){ 
    return (a > b)? a : b;
    } 

    /* Função recursiva principal */
int funcao_mochila(int Mochila, int Peso[], int Valor[], int NumItens){ 
   
    /* Condição para parar: quando acabar os itens ou a  mochila estiver cheia */
   if (NumItens == 0 || Mochila == 0){
       return 0;

    /* Condição quando o item em questão não couber na mochila */
   }if (Peso[NumItens-1] > Mochila){ 
       return funcao_mochila(Mochila, Peso, Valor, NumItens-1);

    /* Parte principal da função: retorna o valor maximo possivel em reais */
   }else{
       return max( Valor[NumItens-1] + funcao_mochila(Mochila-Peso[NumItens-1],
        Peso, Valor, NumItens-1),funcao_mochila(Mochila, Peso, Valor, NumItens-1));
   }

}
  
int main(){ 
    
    /* Os itens são divididos em 2 vetores: valor e peso */
    /* Cada item está separado por indice no vetor: vetor peso e valor no indice 1
        representa o peso e o valor do item 1, por exemplo*/
    int Valor[] = {3, 6, 9};    /* Vetor de valores */
    int Peso[] = {2, 3, 6};     /* Vetor de peso */
    int Mochila = 10;           /* Capacidade da mochila */
    int NumItens = sizeof(Valor)/sizeof(Valor[0]); /* Apenas para pegar a quantidade de itens */
    printf("Valor máximo será: R$ %d \n", funcao_mochila(Mochila, Peso, Valor, NumItens)); 
    return 0; 
}