while True: 
    print("\n=== MENU PRINCIPAL ===")
    opcao = input("Escolha uma opção:\n[1] Fazer Login\n[2] Cadastrar\n[3] sair do programa\nOpção: ")

    if opcao == '1':
        print("tela de login:")
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == "admin" and senha == "1234":
            print("login feito")
        else:
            print("erro")

    elif opcao == '2':
        print("tela de cadastro")
        idade = int(input('digite sua idade?: '))
        altura = float(input('qual sua altura?: '))
        habilitação = input('você tem habilitação? (s/n): ').lower()
        print("qual a sua nacionalidade?: ")
        nacionalidade = input('\n[1] Brasileiro\n[2] outro: ')

        nacionalidade_valida = (nacionalidade == '1' or nacionalidade == '2')

        if idade >= 20 and altura >=1.70 and habilitação == 's' and nacionalidade_valida:
            print('cadastro feito')
        else:
            print('erro')
        
    elif opcao == '3':
        print("\nSaindo do sistema... Até logo!")
        break  # Única forma de quebrar o 'while True' e fechar o programa

    else:
        print("\n→ Opção inválida! Escolha 1, 2 ou 3.")