## Esse projeto é uma simples calculadora de valor crítico de artefatos para o Genshin Inpact.

### Para iniciar o projeto, apenas execute 

#### Subindo o docker

```
docker-compose up -d
```

#### Instalando o poetry

```
poetry install
```

#### Executando as migrations

```
poetry run python manage.py makemigrations

poetry run python manage.py migrate
```

#### Criando um superusuário

```
poetry run python manage.py createsuperuser
```

#### Executando o projeto

```
poetry run python manage.py runserver
```

## Imagem do projeto localmente
![Captura de tela de 2025-06-14 19-46-19](https://github.com/user-attachments/assets/6ca07b26-3d8b-4711-9fdd-6ce3b01b82b9)

