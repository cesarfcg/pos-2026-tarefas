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

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgxOTgyNjAwLCJpYXQiOjE3ODE4OTYyMDAsImp0aSI6IjI3YTM1ZmYxMmNlZDRhNzViOWFjOWZlMjIyNGExMzgwIiwidXNlcl9pZCI6MzY5ODIxfQ.E7gKDZlVQcsibOyV2RzGnyeJ7XgydfdxlgA5K7Pja8k"
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
    print(f"{x["disciplina"]}\nnota etapa 1: {x["nota_etapa_1"]["nota"]} - nota etapa 4: {x["nota_etapa_1"]["nota"]} - nota etapa 3: {x["nota_etapa_3"]["nota"]} - nota etapa 4: {x["nota_etapa_4"]["nota"]}")
   