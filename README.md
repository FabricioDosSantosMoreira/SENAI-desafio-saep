# 📝 Desafio SAEP - SENAI

Resolução do desafio SAEP aplicado pelo SENAI-SC utilizando **Django** e **MySQL**.


## 🌎 Tecnologias Utilizadas

- Python
- Django
- Django-environ
- MySQL | SQLite
- HTML5 | CSS | JS


## 🖼 Galeria
|                                                              |                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------|
| ![Home](./docs/img/Home.png)                                 | ![Gerenciar Tarefas](./docs/img/Gerenciar%20Tarefas.png)               |
| ![Cadastro de Usuário](./docs/img/Cadastro%20Usuário.png)    | ![Cadastro de Tarefa](./docs/img/Cadastro%20Tarefa.png)                |


## ⚙ Instalação

### 🔹 Clone o repositório
```bash
git clone https://github.com/FabricioDosSantosMoreira/SENAI-desafio-saep.git
```

### 🔹 Instale as dependências

```bash
# ⭕ OBS - Necessário ter o MAKE:
make install

# Ou, utilize:
pip install poetry
cd ./desafio/
poetry install
```

### 🔹 Configure o MySQL (Opcional)

```bash
# ⭕ OBS - Necessário ter o MySQL:
Crie um banco de dados localmente com o script localizado em `./docs/Banco de Dados.sql` usando o `MySQL` e contendo:
- Host = `localhost`
- Port = `3306`
- Pass = `123456`

# Ou, se preferir você pode mudar as configurações em: `./desafio/.env`.
```


## 🟢 Execução
```bash
# ⭕ OBS - Necessário ter o MAKE:

# Executa usando o SQLite built-in do Django
make first-sqlite-run

# Executa utilizando o MySQL previamente configurado
make first-mysql-run

# Ou, utilize:
set USE_SQLITE=False  # USE_SQLITE pode ser False ou True, caso seja True usará o SQLite. Caso Falso usará o MySQL.
cd ./desafio/
poetry run python manage.py makemigrations app
poetry run python manage.py migrate
poetry run python manage.py runserver



# 🔄 Para executar o projeto novamente:
make run

# Ou, utilize:
cd ./desafio/
poetry run python manage.py runserver
```


## 💡 Contribuição

Sinta se livre para contribuir com qualquer sugestão, correção ou dicas. Basta abrir um pull request!


## 📃 Licença

O projeto é licensiado sob a licença do MIT. Veja a [Licença](LICENSE/) para mais informações.
