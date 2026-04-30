import json

# Importar de um arquivo
with open('../tarefa09/imobiliaria.json') as json_file:
    parsed_imobiliaria = json.load(json_file)
    imoveis = parsed_imobiliaria['imobiliaria']['imoveis']
while True:
    print("----- Imóveis : ------")
    for x in range(len(imoveis)):
         x = x + 1
         print("Imovel", x)
    x = int(input("Qual imóvel deseja consultar? (Digite o número do índice): "))
    if x > 0 and x <= len(imoveis):
            imovel_selecionado = imoveis[x-1]
            print(f"Descrição: {imovel_selecionado['descricao']}")
            print(f"Endereço: {imovel_selecionado['endereco']}")
            print(f"Proprietário: {imovel_selecionado['proprietario']}")
            print(f"Características: {imovel_selecionado['caracteristicas']}")
            print(f"Valor: {imovel_selecionado['valor']}")
    else:
        print("Número do índice inválido.")
    final = input("Deseja consultar outro imóvel? (s/n): ")
    if final != 's':
        break