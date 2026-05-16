import requests
API_URL = "https://jsonplaceholder.typicode.com/users"

def listar():
    response = requests.get(API_URL)
    inf = response.json()
    if response.status_code == 200:
        return inf
    else:        
        return False 

def ler(user_id):
    response = requests.get(f"{API_URL+"/"+user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return False
def criar(content):
    response = requests.post(API_URL, json=content)
    if response.status_code == 201:
        return response.json()
    else:
        return False

def deletar(user_id):
    response = requests.delete(f"{API_URL+"/"+user_id}")
    if response.status_code == 200:
        return True
    else:        
        return False

def atualizar(user_id, content):
    response = requests.put(f"{API_URL+"/"+user_id}", json=content)
    usu_novo = response.json()
    if response.status_code == 200:
        return usu_novo
    else:        
        return False
