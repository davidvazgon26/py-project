import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Creando la instancia de FastAPI
app = FastAPI()

# Para probar funciones creamos esta ruta con un decorador para el navegador
@app.get('/')
def get_list():
    return[1,2,3]

# Otra ruta de ejemplo
@app.get('/contacto')
def get_list():
    return {
        'name' : 'Demostenes',
    }

# Responder con HTML
@app.get("/items", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Aqui respondiendo con HTML desde el response</h1>
        </body>
    </html>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()  