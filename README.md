# Iniciando com Django REST Framework

Esse simples repositório tem como objetivo servir como para a criação de outros projetos. Atualmente, além do tradicional [django-rest-framework](https://www.django-rest-framework.org/) para a criação de API Web, foi adicionado o [django-ninja](https://django-ninja.rest-framework.com) que usa o Swagger.

## Primeiros passos

O ideal é criar um ambiente de desenvolvimento virtual para rodar o projeto. Geralmente, é recomendado o uso do `virtualenv`.

Nesse [link](https://github.com/cauachagas/cling-torch#passo-1---instalando-miniconda) mostro como instalar o `miniconda` e criar um ambiente de desenvolvimento. Útil para criação de ambientes virtuais com dependências fora do Python, como compiladores e utilitários.

## Como rodar o projeto

1. Clone o repositório;
2. Crie um ambiente de desenvolvimento;
3. Ative o ambiente do passo anterior;
4. Instale as dependências;
5. Faça as migrações;
6. Inicie o servidor.

Usando o módulo `venv` para a criação do ambiente virtual, os passos serão esses

```bash
git clone https://github.com/cauachagas/django-rest-api-exemplo
cd django-rest-api-exemplo
python3 -m venv venv
source venv/bin/activate
python manage.py makemigrations livros
python manage.py migrate
python manage.py runserver
```

Em seguida abra o link http://localhost:8000/ no seu navegador.

## OpenAPI

Para ver a documentação da API, abra o link http://localhost:8000/api/docs no seu navegador.

![](https://drive.google.com/uc?export=view&id=1v8oPPN6gUdxMPRqS5DUGnTAzwJjruMMI)

## Referências

- https://www.udemy.com/course/crie-restful-api-com-django-rest-framework-para-qualquer-um/
- https://www.django-rest-framework.org/
- https://django-ninja.rest-framework.com/