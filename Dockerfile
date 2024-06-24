# Usa la imagen base de Python oficial
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY . .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para que Flask pueda escuchar las solicitudes HTTP
EXPOSE 5000

# Comando por defecto para ejecutar tu aplicación Flask cuando el contenedor se inicie
CMD ["python", "main.py"]