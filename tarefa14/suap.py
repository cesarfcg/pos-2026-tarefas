import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br"
#
# user = input("user: ")
# password = getpass()
#
# data = {"username":user,"password":password}
#
# response = requests.post(api_url+"token/pair", json=data)
# token = response.json()["access"]
# print(response.json())

headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)

ano_letivo = int(input("Digite o ano letivo:"))
periodo_letivo = int(input("Digite o periodo letivo:"))

URL = f"/api/ensino/meu-boletim/{ano_letivo}/{periodo_letivo}/"
response = requests.get(api_url+URL, headers=headers)

print(response.text)
print(response.json())
disciplinas = response.json()["results"]
for x in disciplinas:
    print(f"{x["disciplina"]}\n - nota etapa 1: {x["nota_etapa_1"]["nota"]}\n- nota etapa 2: {x["nota_etapa_2"]["nota"]}\n - nota etapa 3: {x["nota_etapa_3"]["nota"]}\n - nota etapa 4: {x["nota_etapa_4"]["nota"]}")
   