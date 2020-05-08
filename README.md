# Python Template

Esse repositório tem o foco de ser utilizado como template para a criação das novas aplicações


Para este projeto estamos utilizando um padrão baseado em [MVC](https://www.geeksforgeeks.org/mvc-design-pattern/) porém como Python é Multi Paradigma sinta-se a vontade para utilizar classes ou não da maneira que preferir

# Importante

Criar os seguintes secrets no repositório do GitHub da sua aplicação após cria-la a partir do template.

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY

Solicitar o valor de cada uma delas ao Lucas.

## Pré Requisitos

> [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/README.html)

> Python 3.7+

> [Pre-Commit](https://pre-commit.com/)

> [Docker](https://docs.docker.com/get-docker/)

> [Python virtualenv](https://virtualenv.pypa.io/en/latest/)

## Descrição

Para criar a estrutura da aplicação é necessário rodar o cookiecutter para assim gerar o template e substituir as variavéis.

## Criando a aplicação a partir do template

```shell
git clone https://github.com/missing-io/python-template-repo.git
cookiecutter python-template-repo
```

Será feita algumas perguntas para você sobre o nome da aplicação, especificação de memória e CPU, responda

```shell
app_name [name of your application]: my-app
request_memory [Request memory for your application, eg: 512]: 512
request_cpu [Request CPU for your application, eg: 256]: 256
```
Após isso uma pasta será criada com o nome que você colocou no app_name, nessa caso **my_app**

## Como Testar

```shell
cd my-app && virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python my-app.py
```

O Seguinte output será exibido no terminal:

```shell
 * Serving Flask app "src.flask_config" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 202-738-973
```

Execute o seguinte comando apontando para a sua aplicação:
```shell
curl -IL -XGET http://localhost:5000/health/
```

Retorno:
```shell
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 21
Server: Werkzeug/1.0.1 Python/3.8.2
Date: Mon, 04 May 2020 16:22:10 GMT
```
## License

Copyright © 2019 missing-io. All rights reserved.
