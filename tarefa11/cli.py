import users_wrapper as user 
while True:
    opcoes = input("Digite: \n" 
    "1 - Listar usuários\n" 
    "2 - Criar usuário\n" 
    "3 - Ler usuário\n" 
    "4 - Atualizar usuário\n" 
    "5 - Deletar usuário\n"
    "6 - Sair\n")
    if opcoes == "1":
        user.listar()
    elif opcoes == "2":
        new_user = { "name": input("Digite o nome do user"), 
                    "username": input("Digite o username do user"), 
                    "email": input("Digite o email do user"),
                     "address": {
                        "street": input("Digite a rua do user"),
                        "suite": input("Digite a suite do user"),
                        "city": input("Digite a cidade do user"),
                        "zipcode": input("Digite o zipcode do user"),
                        "geo": {
                            "lat": input("Digite a latitude do user"),
                            "lng": input("Digite a longitude do user")
                        },
                        "phone": input("Digite o telefone do user"),
                        "website": input("Digite o website do user"),
                        "company": {
                               "name": input("Digite o nome da empresa do user"),
                               "catchPhrase": input("Digite a catchPhrase da empresa do user"),
                               "bs": input("Digite o bs da empresa do user")
                    }}
                    }
        
        user.criar(new_user)
    elif opcoes == "3":
        user_id = input("Digite o ID do usuário que deseja ler: ")
        user.ler(user_id)
    elif opcoes == "4":
        user_id = input("Digite o ID do usuário que deseja atualizar: ")
        put_user = { "name": input("Digite o novo nome do user"), 
                         "username": input("Digite o novo username do user"), 
                         "email": input("Digite o novo email do user"),
                          "address": {
                             "street": input("Digite a nova rua do user"),
                             "suite": input("Digite a nova suite do user"),
                             "city": input("Digite a nova cidade do user"),
                             "zipcode": input("Digite o novo zipcode do user"),
                             "geo": {
                                 "lat": input("Digite a nova latitude do user"),
                                 "lng": input("Digite a nova longitude do user")
                             },
                             "phone": input("Digite o novo telefone do user"),
                             "website": input("Digite o novo website do user"),
                             "company": {
                                    "name": input("Digite o novo nome da empresa do user"),
                                    "catchPhrase": input("Digite a nova catchPhrase da empresa do user"),
                                    "bs": input("Digite o novo bs da empresa do user")
                                }
                         }}
        user.atualizar(user_id, put_user)
    elif opcoes == "5":
        user_id = input("Digite o ID do usuário que deseja deletar: ")
        confirmacao = input(f"Tem certeza que deseja deletar o usuário com ID {user_id}? (s/n): ")
        if confirmacao == 's':
            user.deletar(user_id)
        else:
            print("Operação de deleção cancelada.") 
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
