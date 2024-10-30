# SENAI - Desafio SAEP


## ⚙ Instalação

### 🔹 Clone o repositório do projeto

```bash
git clone https://github.com/FabricioDosSantosMoreira/SENAI-desafio-saep.git
```

### 🔹 Instale as dependências do projeto

```bash
make install
```

### 🔹 Configure o MySQL (Opcional)

Crie um novo banco de dados localmente usando o `MySQL`, contendo:
- Host= `localhost`
- Port= `3306`
- Pass = `123456`


O script de criação está em: docs/Banco de Dados.sql
Ou, se preferir você pode mudar as configurações em: `core/config.py`.



## 🟢 Execução do 

Utilize o `Make` para executar o projeto:

```bash
make first-sqlite-run
```

Ou (OBS: Necessário ter o MySQL previamente configurado)
```bash
make first-mysql-run 
```
