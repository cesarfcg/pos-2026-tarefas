from xml.dom.minidom import parse
dom = parse(' ')
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName('prato')

for prato in pratos:
    i = input(f'nome do prato: {prato.getAttribute("nome")}, id do prato: {prato.getAttribute("id")}')
    print(i)
