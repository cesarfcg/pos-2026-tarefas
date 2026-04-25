from xml.dom.minidom import parse
dom = parse('../tarefa04/cardapio.xml') 
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName('prato')
while True:
    print("----- Pratos disponíveis: ------")
    for prato in pratos:
        nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue.strip()
        id = prato.getAttribute("id")
        print(F'{id} | {nome}')
    print("--------------------------------")
    input_id = int(input("Digite o id do prato para saber mais detalhes: "))
    print("--------------------------------")

    if input_id <= len(pratos):
        prato_selecionado = pratos[int(input_id)-1]
        descricao = prato_selecionado.getElementsByTagName("descricao")[0].firstChild.nodeValue.strip()
        ingrediente = prato_selecionado.getElementsByTagName("ingrediente")[0].firstChild.nodeValue.strip()
        preco = prato_selecionado.getElementsByTagName("preco")[0].firstChild.nodeValue.strip()
        calorias = prato_selecionado.getElementsByTagName("calorias")[0].firstChild.nodeValue.strip()
        tempo_preparo = prato_selecionado.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue.strip()
        lista_ingredientes = []

        for x in prato_selecionado.getElementsByTagName("ingrediente"):
            ingrediente = x.firstChild.nodeValue.strip()
            lista_ingredientes.append(ingrediente)
        print(f"Descrição: {descricao}")
        print("Ingredientes:")

        for ing in lista_ingredientes:
            print(f"- {ing}")
        print(f"Preço: {preco}")
        print(f"Calorias: {calorias}")
        print(f"Tempo de preparo: {tempo_preparo}")
        print("--------------------------------")

    else:    
        print("Id inválido.")
    final = input("Deseja consultar outro prato? (s/n): ")
    if final != 's':
        break

