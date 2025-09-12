FROM python:3.9-slim

WORKDIR /app

# Copiar o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos do projeto para o diretório de trabalho
COPY . .

# Expor a porta 5000 para que possamos nos conectar ao app
EXPOSE 5000

# Comando para executar a aplicação quando o container iniciar
CMD ["python", "app.py"]
