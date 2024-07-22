#!/bin/sh

# Inicia el servidor de Ollama en segundo plano
ollama serve &

# Espera un momento para asegurarse de que Ollama esté completamente iniciado
sleep 10

# Inicia la aplicación Flask
exec python app.py
