# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
#Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
def meses(mm):
    mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return mes[mm - 1]

def verificar_Data(d, mm, aaa):
    # Verifica se o ano, mês e dia estão dentro de limites válidos
    if mm < 1 or mm > 12 or d < 1 or d > 31:
        return 'Dia ou Mês incorreto'
    # Verifica o número de dias em cada mês
    if mm in [4, 6, 9, 11] and d > 30:
        return 'O dia não corresponde ao mês'
    if mm == 2:  # Fevereiro
        #Se o ano for divisível por 4 : O ano será bissexto, exceto se ele também for divisível por 100
        #Se o ano for divisível por 100 e não for divisível por 400 : O ano não será bissexto
        #Se o ano for divisível por 400 : O ano será bissexto
        if (aaa % 4 == 0 and aaa % 100 != 0) or (aaa % 400 == 0):
            if d > 29:
                return "Mês com menos de 29 Dias"
        else:
            if d > 28:
                return "Mês com menos de 28 Dias"


def separando_Valor(data):
    try:
        d, mm, aaa = map(int, data.split('/'))
    except: 
        return 'Erro'
    else: 
        verificar_Data(d, mm, aaa)
    
    if verificar_Data(d, mm, aaa):
        response = verificar_Data(d, mm, aaa)
        return response
    else: 
        return f'{d} de {meses(mm)} de {aaa}'

data = input()
print(separando_Valor(data))
