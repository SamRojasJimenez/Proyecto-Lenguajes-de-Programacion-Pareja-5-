FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias
RUN pip install --no-cache-dir mysql-connector-python

# Copiar el script
COPY report.py .

# Ejecutar el script (en un bucle para simular tarea programada o simplemente activarlo)
CMD ["python", "-u", "report.py"]
