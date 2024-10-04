# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
#Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
def separando_Valor(data):
    
    D, MM, AAA = map(int, data.split('/'))
    return D, MM, AAA
    

data = input()
print(separando_Valor(data))
