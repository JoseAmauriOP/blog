# Django Blog Project

Este é um projeto de um sistema de blog completo desenvolvido utilizando o framework **Django**.

## 📋 Funcionalidades

- **Listagem de Posts**: Exibição de todos os posts publicados em ordem cronológica.
- **Leitura Detalhada**: Página dedicada para leitura completa de cada artigo.
- **Sistema de Comentários**: Usuários podem deixar comentários nos posts.
- **Status de Publicação**: Controle de posts como "Rascunho" (Draft) ou "Publicado" (Published).
- **URLs Amigáveis**: Slugs personalizados para cada postagem baseados na data de publicação.

## 🛠️ Tecnologias Utilizadas

- **Python** (3.x)
- **Django** (6.0)
- **SQLite** (Banco de dados padrão)
- **HTML/CSS** (Templates e estilização)

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o projeto em seu ambiente local.

### Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina.

### Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/JoseAmauriOP/blog.git
   cd blog
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realize as migrações do banco de dados**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (Opcional - para acessar o admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

7. **Acesse o projeto**
   - Abra o navegador e vá para: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Para acessar a área administativa: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📂 Estrutura do Projeto

- **blog/**: Aplicação principal contendo models, views e templates.
- **config/**: Configurações globais do projeto Django.
- **manage.py**: Utilitário de linha de comando do Django.
- **db.sqlite3**: Banco de dados local.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---
Desenvolvido por José Amauri