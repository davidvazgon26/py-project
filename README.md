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


## Implementando Docker

* Crea en cada proyecto el archivo Dockerfile 
* Agregar las configuraciones necesarias por ejemplo:

````
FROM python:3.8
WORKDIR /app
RUN ls -la /app
COPY requirement.txt /app/requirement.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirement.txt
COPY . /app/
CMD bash -c "while true; do sleep1; done"
````

* Ahora crea un archivo docker-compose.yml con parametros, por ejemplo:
````
services:
  app-csv:
    build:
      context: .
      dockerfile: Dockerfile
````

* Construimos y arrancamos el contenedor con los siguientes comandos:
````
docker-compose build
docker-compose up -d
docker-compose ps
````

* Hasta aqui ya creamos el contenedor, lo ejecutamos y verificamos que esta corriendo, ahora vamos a utilizarlo con el siguiente comando (considerar que el nombre debe cambiar segun el nombre del contenedor que tienes en SERVICE cuando corres el ultimo comando).

````
docker-compose exec app-csv bash
````

* dentro del contenedor puedes utilizar los comandos como los usarias normalmente, como si fuera un ambiente env, para salir solo debes digitar **exit**

* Para apagar el contenedor utiliza down, aqui los comandos:
````
exit 
docker-compose down
````

* Si necesitas modificar el contenedor, realizas tus cambios, vuelves a re construir el contenedor y ejecutas.
````
docker-compose build
.
.
.
.
````


 