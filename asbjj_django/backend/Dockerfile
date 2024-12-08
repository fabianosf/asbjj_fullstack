# Usar imagem oficial do Python 3.10
FROM python:3.10-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y libpq-dev

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt e instalar dependências
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copiar o código fonte
COPY . /app/

# Expor a porta do Django
EXPOSE 8000

# Comando para rodar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
