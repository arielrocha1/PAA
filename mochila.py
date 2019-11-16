    # Importa a biblioteca de combinatória
from itertools import combinations
 
    # Retorna todas as combinações possíveis
def anycomb(Itens):
    ' return combinations of any length from the Itens '
    return ( comb
             for i in range(1, len(Itens)+1)
             for comb in combinations(Itens, i)
             )
 
    # Calcula o total de peso e valor dessa combinação
def ValorTotal(comb):
    PesoTotal = 0
    ValorTotal = 0
    for item, Peso, Valor in comb:
        PesoTotal  += Peso
        ValorTotal += Valor
    return (ValorTotal, -PesoTotal) if PesoTotal <= 20 else (0, 0)
 
    # Lista de itens Disponíveis
Itens = (
    ("Dicionário", 2, 3), ("Diário", 3, 6), ("Caderno", 6, 9),
    ("Fichário", 10, 15),
    )

Mochila = max( anycomb(Itens), key=ValorTotal) 

print("Itens selecionados foram: \n  * " +'\n  * '.join(sorted(item for item,_,_ in Mochila))) # Imprime os itens 1 por 1

Valor, Peso = ValorTotal(Mochila) # Calcula peso e valor total

print("Maior valor possível é R$%i.00 com o peso de %i kg" % (Valor, -Peso)) # Resultado final