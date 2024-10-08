# Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
# Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
import random
import math
def aleatorio(palavra, separa):
    lista= []
    
    for i in range(separa):
        embaralhar = random.shuffle(palavra)
        junta = ''.join(palavra)
        lista.append(junta)
        
    sem_repetir = set(lista)
    return sem_repetir



palavra = list(input().lower())
# calcula a quantidade de possibilidade da palavra
separa = math.factorial(len(palavra))

# Calcula a quantidade de possibilidade da palavra
resultados = aleatorio(palavra, separa)

# Exibe as permutações em um formato organizado
print ("A forma que a palavra pode ser escrita é:")
for perm in resultados:
    print(perm)