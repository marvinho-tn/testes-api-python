# 🧪 Testes API Python

Este projeto demonstra três implementações diferentes de uma API de conselhos (**Flask**, **Django** e **FastAPI**) utilizando uma biblioteca compartilhada (`shared-lib`) para centralizar lógica e modelos.

## 📂 Estrutura do projeto

```
testes-api-python/
├── django/       # API em Django
├── fast/         # API em FastAPI
├── flask/        # API em Flask
└── shared-lib/   # Biblioteca compartilhada (src/shared)
```

---

## ⚙️ Instalação da shared-lib

Antes de rodar qualquer API, instale a biblioteca compartilhada localmente:

```bash
cd shared-lib
pip install -e .
```

Isso instala a lib em modo **editable**, permitindo que alterações em `src/shared` sejam refletidas automaticamente nas APIs.

---

## ⚙️ Configuração de ambiente (`.env`)

Cada API possui sua própria pasta e deve conter um arquivo `.env` com variáveis específicas.  
Esses arquivos **não são versionados no Git** (já estão no `.gitignore`).

### 📜 Django (`django/.env`)
```env
APP_NAME=Minha API Django
ADVICE_API_BASE_URL=https://api.adviceslip.com
```

---

### 📜 Flask (`flask/.env`)
```env
APP_NAME=Minha API Flask
ADVICE_API_BASE_URL=https://api.adviceslip.com
```

---

### 📜 FastAPI (`fast/.env`)
```env
APP_NAME=Minha API FastAPI
ADVICE_API_BASE_URL=https://api.adviceslip.com
```

---

## 🧠 Observações

- Cada framework lê o `.env` com sua própria lib (`python-dotenv` ou equivalente).

---

## 🚀 Rodando as APIs

### 1. Flask

```bash
cd flask
pip install -r requirements.txt
python main.py
```

Acesse em:  
👉 `http://127.0.0.1:5000`

---

### 2. Django

```bash
cd django
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse em:  
👉 `http://127.0.0.1:8000/`

---

### 3. FastAPI

```bash
cd fast
pip install -r requirements.txt
uvicorn main:app --reload
```

Acesse em:  
👉 `http://127.0.0.1:8000/`

---

## 🧠 Observações

- Todas as APIs usam a **shared-lib** para lógica e schemas.
- Os endpoints básicos implementados são:
  - `GET /` → Hello World
  - `GET /items/<id>?q=...` → retorna id + query
  - `GET /advices` → retorna conselho aleatório de uma API externa