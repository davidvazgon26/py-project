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
python3 -m venv env
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

Crear para cada proyecto en su propio ambiente el ambiente virtual, entrar en cada carpeta o proyecto y crearlo con el siguiente comando:
```
python3 -m venv env
```

Activar el ambiente:
```
source env/bin/activate
```
Nota.- debes estar en el directorio del proyecto para activar el ambiente.

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
Nota.- este comando veras las librerias o paquetes instalados del ambiente en el que estes.

Para automatizar la instalacion de dependencias utilizaremos para crear el archivo base:
```
pip3 freeze > requirements.txt
```

Luego para consumirlo e instalar las dependencias necesarias utilizamos el comando:
```
pip3 install -r requirements.txt
```


### Proyectos

En esta carpeta existen varios proyectos con su propio ambiente virtual, los proyectos actuales son:

* app
* appPandas
* charts
* game
* web-server

 