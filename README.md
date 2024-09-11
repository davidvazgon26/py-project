# Game Project

Para correr el juego debes ingresar los siguientes comandos en la terminal, dentro de la ruta del proyecto.

```sh
cd game
python3 main.py
```
Siguientes pasos aqui abajo...

# App Project

Para correr el juego debes ingresar los siguientes comandos en la terminal, dentro de la ruta del proyecto.

```sh
git clone "url de github"
cd app
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

# Otros Comandos utiles

## Verificar donde esta python y pip

```
which python3
which pip3
```
Si estas en linux o wsl debes instalar
```
sudo apt install -y python3-venv
```

Poner cada proyecto en su propio ambiente, entrar en cada carpeta:
```
python3 -m venv env
```

Activar el ambiente:
```
source env/bin/activate
```

Salir del ambiente virtual:
```
deactivate
```

Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo:
```
pip3 install matplotlib==3.5.0
```

Verificar las instalaciones:
```
pip3 freeze
```

Para automatizar la instalacion de dependencias utilizaremos para crear el archivo base:
```
pip3 freeze > requirements.txt
```

Luego para consumirlo e instalar las dependencias necesarias utilizamos el comando:
```
pip3 install -r requirements.txt
```

 