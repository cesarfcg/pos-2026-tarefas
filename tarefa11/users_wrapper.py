import requests
API_URL = "https://jsonplaceholder.typicode.com/users"
def listar():
    response = requests.get(API_URL)
    inf = response.json()
    if response.status_code == 200:
        print(inf)

def ler(user_id):
    response = requests.get(f"{API_URL+"/"+user_id}")
    if response.status_code == 200:
        print (response.json())

def criar(content):
    response = requests.post(API_URL, json=content)
    if response.status_code == 201:
        print("User criado",response.json())

def deletar(user_id):
    response = requests.delete(f"{API_URL+"/"+user_id}")
    if response.status_code == 200:
        print(f"User {user_id} foi deletado")

def atualizar(user_id, content):
    response = requests.put(f"{API_URL+"/"+user_id}", json=content)
    u = response.json()
    if response.status_code == 200:
        print(f"Usuário id {u['id']} atualizado")
    else:
        print("erro")
