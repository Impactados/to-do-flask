# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo de dependências e instalar as dependências
COPY config/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código da aplicação para o contêiner
COPY . .

# Definir variáveis de ambiente
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expor a porta em que o Flask será executado
EXPOSE 5000
