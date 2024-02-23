import os

def exibir_nome_do_programa():
    print("""
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """)

#https://fsymbols.com/pt/

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Cadastrar restaurante')
    print('4. Sair\n')

def finalizar_app():
   os.system('cls')
   print('Finalizando o app')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listrar restaurantes')   
    elif opcao_escolhida == 3:
        print('Ativar restaurante')   
    else:
        finalizar_app()  


def main():
   exibir_nome_do_programa()
   exibir_opcoes()
   escolher_opcao()
   

if __name__ == '__main__':
    main()

