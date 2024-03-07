# Nome do Projeto

Breve descrição do projeto.

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Configuração Inicial

1. **Clonar o repositório**

```
git clone https://github.com/Impactados/to-do-flask.git
cd to-do-flask
```

# Construir e rodar o projeto usando Docker Compose
Para ambientes de desenvolvimento e produção, você terá arquivos de configuração do Docker Compose separados. A seguir, são apresentadas as instruções para executar o projeto em cada ambiente.

## Desenvolvimento
No ambiente de desenvolvimento, o Docker Compose utiliza o arquivo docker-compose.override.yml (se presente) junto com o docker-compose.yml por padrão.

1. **Iniciar o projeto**
```
docker-compose up --build
```
> Esse comando constrói a imagem do seu aplicativo (se necessário) e inicia os serviços definidos no seu docker-compose.yml e docker-compose.override.yml.

2. **Parar o projeto**
```
docker-compose down
```

## Produção
No ambiente de produção, você utilizará o docker-compose.prod.yml para sobrescrever ou adicionar configurações específicas de produção.
1. **Enviroments**
Crie um arquivo .env na raiz do projeto e preencha-o com as variáveis de ambiente necessárias para produção. Exemplo:
```
DATABASE=prod_database
USER=prod_user
PASSWORD=your_secure_password
SECRET=your_secret_key
```

2. **Iniciar o projeto em produção**
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build
```
> Esse comando instrui o Docker Compose a usar a configuração base junto com as configurações específicas de produção.

3. **Parar o projeto em produção**
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
```

# Acessar o Aplicativo
Após iniciar o aplicativo, você pode acessá-lo abrindo http://localhost:5000 no seu navegador, assumindo que o docker-compose mapeou a porta 5000 do contêiner para a porta 5000 do seu host.