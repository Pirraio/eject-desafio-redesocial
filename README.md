# Desafio EJECT Rede Social API

## Sobre o projeto

Uma API REST simulando uma rede social em que usuários possam se cadastrar e fazer login para ter uma experiência básica de uma rede social, podendo realizar postagens, visualizar postagens, comentar em postagens de outros usuários, entre outros.

## Instalação e Execução
1. No seu terminal, clone o repositório.
    ```
    git clone https://github.com/Pirraio/eject-desafio-redesocial.git
    ``` 
2. Acesse a pasta criada com o comando `cd`.
    ```
    cd eject-desafio-redesocial
    ``` 
3. Crie e ative um ambiente virtual com os seguintes comandos:
    ### Windows
    ```
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
    ### Linux e MacOS
    ```
    $ python -m venv .venv
    $ source myvenv/bin/activate
    ```
4. Agora, execute o seguinte comando para instalar todas as dependências do projeto.
    ```
    pip install -r requirements.txt
    ```
5. Crie um super usuário para ter permissões de administrador na API.
    ```
    python .\manage.py createsuperuser
    ```
6. Execute esse comando para rodar o projeto.
    ```
    python .\manage.py runserver
    ``` 
7. Acesse no seu navegador a seguinte url:
    ```
    http://127.0.0.1:8000/
    ```

## Instruções de uso da API
Depois de acessar a URL `127.0.0.1:8000`, você precisa se autenticar para poder utilizar a API. Você pode alcançar isso criando um novo usuário na rota:
```
127.0.0.1:8000/cadastrar
```
Após cadastrar um usuário, é necessário autenticá-lo. Você pode fazer isso com o super usuário (caso tenha criado anteriormente) ou com o usuário criado na rota de cadastrar. Para autenticar, acesse:
```
127.0.0.1:8000/token
```
Pronto! Agora você está autenticado e já consegue acessar os endpoints da API pelo seu navegador. Tenha em mente que após um tempo o seu token de acesso pode expirar, é possível renová-lo realizando um POST após acessar a rota:
```
127.0.0.1:8000/token/refresh
```

## Documentação da API
É possível acessar a documentação da API para visualizar todos os endpoints disponíveis na API. Com o servidor funcionando, acesse:
```
127.0.0.1:8000/swagger
127.0.0.1:8000/redoc
```

## Dependências
Para garantir que o projeto funcione corretamente, certifique-se de possuir Python e de realizar a instalação dos pacotes requeridos com o `pip`. 
- Python 3.13  
- Django 5.1.4  
- Django REST framework 3.15.2
- Git 2.46 (Opcional)