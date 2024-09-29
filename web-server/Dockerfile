
# Laversion de python con la que correra el proyecto
FROM python:3.10

# El directorio de trabajo
WORKDIR /app
# Crear una copia de nuestro requirement en el ambiente de Docker (local/contenedor)

# Para validar que este en la ruta correcta
RUN ls -la /app

COPY requirement.txt /app/requirement.txt

# Instalar dependencias del archivo requirements.txt y actualizar dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirement.txt

# Ahora crear copia de nuestro codigo en el ambiente de Docker

COPY . /app/


# Recuerda que necesitas el archivo docker-compose.yml


# Comando para mantener corriendo el contenedor de Docker
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8080"]