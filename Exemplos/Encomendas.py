encomendas = input("Digite os números das encomendas seperados por vírgula: ").split(',')

try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
        print("Uma das entradas não é um número válido.")