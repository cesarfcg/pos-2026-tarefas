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
        print(user.listar())

    if opcoes == "2":
        new_user = {}
        new_user["name"] = input("Digite o nome do usuário: ")
        new_user["username"] = input("Digite o username do usuário: ")
        new_user["email"] = input("Digite o email do usuário: ")
        new_user["address"] = {
            "street": input("Digite a rua do usuário: "),
            "suite": input("Digite a suite do usuário: "),
            "city": input("Digite a cidade do usuário: "),
            "zipcode": input("Digite o zipcode do usuário: "),
            "geo": {
                "lat": input("Digite a latitude do usuário: "),
                "lng": input("Digite a longitude do usuário: ")
            }
        }
        new_user["phone"] = input("Digite o telefone do usuário: ")
        new_user["website"] = input("Digite o website do usuário: ")
        new_user["company"] = {
            "name": input("Digite o nome da empresa do usuário: "),
            "catchPhrase": input("Digite a catchPhrase da empresa do usuário: "),
            "bs": input("Digite o bs da empresa do usuário: ")
        }
        
        criou = user.criar(new_user)
        if criou:
            print("Usuário criado com sucesso!")
        else:
            print("Falha ao criar usuário.")

    

    if opcoes == "3":
        user_id = input("Digite o ID do usuário que deseja ler: ")
        print(user.ler(user_id))
    
    if opcoes == "4":
        user_id = input("Digite o ID do usuário que deseja atualizar: ")
        put_user = {}
        put_user["name"] = input("Digite o nome do usuário: ")
        put_user["username"] = input("Digite o username do usuário: ")
        put_user["email"] = input("Digite o email do usuário: ")
        put_user["address"] = {
            "street": input("Digite a rua do usuário: "),
            "suite": input("Digite a suite do usuário: "),
            "city": input("Digite a cidade do usuário: "),
            "zipcode": input("Digite o zipcode do usuário: "),
            "geo": {
                "lat": input("Digite a latitude do usuário: "),
                "lng": input("Digite a longitude do usuário: ")
            }
        }   
        put_user["phone"] = input("Digite o telefone do usuário: ")
        put_user["website"] = input("Digite o website do usuário: ")
        put_user["company"] = {
            "name": input("Digite o nome da empresa do usuário: "),
            "catchPhrase": input("Digite a catchPhrase da empresa do usuário: "),
            "bs": input("Digite o bs da empresa do usuário: ")
        }
        
        atualizou = user.atualizar(user_id, put_user)
        if atualizou:
            print("Usuário atualizado com sucesso!")
        else:
            print("Falha ao atualizar usuário.")


    if opcoes == "5":
        user_id = input("Digite o ID do usuário que deseja deletar: ")
        confirmacao = input(f"Tem certeza que deseja deletar o usuário com ID {user_id}? (s/n): ")
        if confirmacao == 's':
            deletou = user.deletar(user_id)
            if deletou:
                print("Usuário deletado com sucesso!")
            else:
                print("Falha ao deletar usuário.")
        else:
            print("Operação de deleção cancelada.") 
    
