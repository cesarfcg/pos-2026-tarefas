import requests
api_url = "https://jsonplaceholder.typicode.com/users"
def list():
    response = requests.get(api_url)
    for user in response.json():
        print(f"User {user['id']}: {user['name']}")
def create():
    new_user = { "name": "John Doe", "username": "johndoe", "email": "johndoe@example.com" }
    response = requests.post(api_url, json=new_user)
    return response.json()
def read():
    response = requests.get(api_url)
    return response.json()
def delete(user_id):
    response = requests.delete(api_url + f"/{user_id}")
    if response.status_code == 200:
        print(f"User {user_id} foi deletado")