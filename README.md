# Iniciando com Django REST Framework

## Primeiros passos

O ideal é criar um ambiente de desenvolvimento virtual para rodar o projeto. Geralmente, recomendam o uso do `virtualenv`. Caso queira fazer deploy de uma aplicação Django no Heroku é melhor usar uma versão `3.6 >= 3.6.x <= 3.6.13` do Python, que pode ser facilmente instalado pelo `miniconda/anaconda`.

Nesse [link](https://github.com/cauachagas/cling-torch#passo-1---instalando-miniconda) mostro como instalar o miniconda e criar um ambiente de desenvolvimento.

## Como rodar o projeto

1. Clone o repositório;
2. Crie um ambiente de desenvolvimento;
3. Ative o ambiente do passo anterior;
4. Instale as dependências;
5. Faça as migraçãos;
6. Crie um super usuário para acessar a interface admin.
7. Inicie o servidor.

Caso use o `miniconda/anaconda` e tenha os scripts `conda` e `activate` no `$PATH` então o passos serão esses

```bash
git clone https://github.com/cauachagas/django-rest-api-exemplo
cd django-rest-api-exemplo
conda env create -f environment.yml
source activate django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Em seguida abra o link http://localhost:8000/ no seu navegador.

## Referências

- https://www.udemy.com/course/crie-restful-api-com-django-rest-framework-para-qualquer-um/

- https://www.django-rest-framework.org/