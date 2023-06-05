# Define a imagem base
FROM python:alpine3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte da aplicação para o diretório de trabalho
COPY . .

# Define a porta em que a aplicação irá escutar
EXPOSE 5000

# Define o comando a ser executado quando o contêiner for iniciado
CMD ["python", "app.py"]