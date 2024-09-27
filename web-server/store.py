import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print("El tipo de dato entregado es: ", type(r.text))
    print("transformando datos a json")
    
    # Convertir el string en una lista de json's
    categories = r.json()
    
    # Ingresar a datos especificos de cada json de la lista
    for category in categories:
        print(category['id'], category['name'])
        