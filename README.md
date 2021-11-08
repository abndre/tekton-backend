# Tekton-backend

# Instalacao

Crie um ambiente virtual:

``` 
pip install -r requirements.txt
```

# Comandos utilizados para criar o servico

```
django-admin startproject tekton
```

Adcionado django-restufull no arquivo [tekton/settints.py](/tekton/tekton/settings.py)

```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Criado um app para cadastro de profissionais,
os comandos abaixo devem ser executados dentro da pasta
tekton, jundo do arquivo [manage.py](tekton/manage.py)

```
python manage.py startapp professional
```

# Testando

Para testar a API do backend, rode o servidor

```
python manage.py runserver
```

E utilize uma ferramenta amigavel, como o [postman](https://www.postman.com/)

Ou teste via curl
```
curl --location --request GET 'http://127.0.0.1:8000/professional/'
```
