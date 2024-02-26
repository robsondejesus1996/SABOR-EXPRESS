projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

"""
try:
    for projeto in projetos:
        print(f"Projeto: {projeto}")
except Exception as e:
    print("Ocorreu um erro: ", e)

"""   

for projeto in projetos:
    if projeto:
        print(f"Projeto: {projeto}")
    else:
        print("Projeto não disponível.")    