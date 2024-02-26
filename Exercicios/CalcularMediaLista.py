lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)        
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é posível calcular a media.")    
except Exception as e:
    print(f"Ocorreu um erro: {e}")    