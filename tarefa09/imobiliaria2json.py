from xml.dom.minidom import parse
import json
dom = parse('../tarefa05/imobiliaria.xml') 
imobiliaria = dom.documentElement
imoveis = imobiliaria.getElementsByTagName('imovel')
imoveis_lista = []
for imovel in imoveis:
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue.strip()

    endereco = imovel.getElementsByTagName("endereco")[0].firstChild.nodeValue.strip()
    rua = imovel.getElementsByTagName("rua")[0].firstChild.nodeValue.strip()
    if imovel.getElementsByTagName("número"):
        numero = imovel.getElementsByTagName("número")[0].firstChild.nodeValue.strip()
    bairro = imovel.getElementsByTagName("bairro")[0].firstChild.nodeValue.strip()
    cidade = imovel.getElementsByTagName("cidade")[0].firstChild.nodeValue.strip()

    proprietario = imovel.getElementsByTagName("proprietario")[0].firstChild.nodeValue.strip()
    nome = imovel.getElementsByTagName("nome")[0].firstChild.nodeValue.strip()
    if imovel.getElementsByTagName("telefone"):
        telefone = imovel.getElementsByTagName("telefone")[0].firstChild.nodeValue.strip()
    if imovel.getElementsByTagName("email"):
        email = imovel.getElementsByTagName("email")[0].firstChild.nodeValue.strip()

    caracteristicas = imovel.getElementsByTagName("caracteristicas")[0].firstChild.nodeValue.strip()
    tamanho = imovel.getElementsByTagName("tamanho")[0].firstChild.nodeValue.strip()
    numQuartos = imovel.getElementsByTagName("numQuartos")[0].firstChild.nodeValue.strip()
    numBanheiros = imovel.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue.strip()
    valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue.strip()

    imoveis_lista.append(

                {
                    "descricao": descricao,
                    "endereco": {
                        "rua": rua,
                        "numero": numero ,
                        "bairro": bairro,
                        "cidade": cidade
                },
                "proprietario": {
                    "nome": nome,
                    "telefone": telefone ,
                    "email": email,
                },
                "caracteristicas": caracteristicas,
                "valor": valor
            }
            
    )
resultado = {
        "imobiliaria": {
            "imoveis": imoveis_lista
        }
    }
with open('imobiliaria.json', 'w') as json_file:
    json.dump(resultado, json_file)