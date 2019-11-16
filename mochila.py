    # Função recursiva principal
def funcao_mochila(Mochila , Peso , Valor , NumItens): 
    
    # Condição para parar: quando acabar os itens ou a  mochila estiver cheia 
    if NumItens == 0 or Mochila == 0 : 
        return 0

    # Condição quando o item em questão não couber na mochila 
    if (Peso[NumItens-1] > Mochila): 
        return funcao_mochila(Mochila , Peso , Valor , NumItens-1) 

    # Parte principal da função: retorna o valor maximo possivel em reais 
    else: 
        return max(Valor[NumItens-1] + funcao_mochila(Mochila-Peso[NumItens-1] , Peso , Valor ,
        NumItens-1),funcao_mochila(Mochila , Peso , Valor , NumItens-1)) 
  

# Os itens são divididos em 2 vetores: valor e peso 
# Cada item está separado por indice no vetor: vetor peso e valor no indice 1
#  representa o peso e o valor do item 1, por exemplo 
Valor = [3, 6, 9]   # Vetor de valores 
Peso = [2, 3, 6]    # Vetor de peso 
Mochila = 10        # Capacidade da mochila 
NumItens = len(Valor)   # apenas para pegar a quantidade de itens 
print("Valor máximo será: R$",funcao_mochila(Mochila , Peso , Valor , NumItens))