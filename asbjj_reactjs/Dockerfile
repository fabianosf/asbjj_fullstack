# Usar imagem oficial do Node.js
FROM node:16

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o package.json e instalar dependências
COPY package.json /app/
RUN npm install

# Copiar o restante do código fonte
COPY . /app/

# Expor a porta usada pelo ReactJS (normalmente 3000, mas pode variar)
EXPOSE 3000

# Comando para rodar o servidor React em modo desenvolvimento
CMD ["npm", "run", "dev"]
