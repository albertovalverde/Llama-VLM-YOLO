# Utiliza una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Instala dependencias del sistema necesarias para la compilación de paquetes Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    git \
    wget \
    curl \
    cmake \
    swig \
    && apt-get clean

# Copia los archivos de tu aplicación al contenedor
COPY . /app

# Instala pip
RUN pip install --upgrade pip

# Instala una versión específica de Werkzeug
RUN pip install Werkzeug==2.0.3

# Instala Flask
RUN pip install Flask==2.1.2

# Instala la biblioteca Ollama
RUN pip install ollama

# Clona e instala LLaMA 3 (si es necesario para tu aplicación)
RUN git clone https://github.com/meta-llama/llama3.git /tmp/llama3 \
    && cd /tmp/llama3 \
    && pip install -e .

# Copia el script de inicio al contenedor
COPY start.sh /app/

# Da permisos de ejecución al script de inicio
RUN chmod +x /app/start.sh

# Expone los puertos necesarios
EXPOSE 5000

# Comando para ejecutar el script de inicio
CMD ["/app/start.sh"]
