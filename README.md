# 📄 Documentação do Projeto — **Gerenciador de Projetos**

## 📌 Visão Geral

Este projeto é um **Gerenciador de Projetos** feito com **Flask**, **HTML/Jinja**, **CSS (Tailwind + personalizado)** e usa **arquivos CSV** para armazenar os dados de **projetos** e **tarefas**.  
O sistema permite:

- Cadastrar novos projetos (com imagem e descrição).
- Visualizar uma lista de projetos cadastrados.
- Editar projetos existentes.
- Adicionar tarefas a cada projeto.
- Remover projetos e tarefas.

---

## 🚀 Como Funciona

### Frontend
- **Homepage (`home.html`)**: Página inicial com botão "Adicionar Projeto".
- **Adicionar Projeto (`addprojeto.html`)**: Formulário para criar um novo projeto, incluindo upload de imagem.
- **Lista de Projetos (`lista_projetos.html`)**: Listagem de todos os projetos com suas respectivas tarefas.
- **Navegação (`nav.html`)**: Barra de navegação fixa no topo.

### Backend (Flask `app.py`)
- `read_projects()`: Lê os projetos do arquivo `projects.csv`.
- `write_projects()`: Salva os projetos no arquivo `projects.csv`.
- `read_tasks()`: Lê as tarefas do arquivo `tasks.csv`.
- `write_tasks()`: Salva as tarefas no arquivo `tasks.csv`.
- Rotas principais:
  - `/` → Página inicial.
  - `/projetos` → Lista todos os projetos.
  - `/addprojeto` → Formulário para adicionar projeto (código ainda incompleto no seu envio).

---

## 📄 Explicação dos Principais Arquivos

### `index.html`
Arquivo base que define:
- Inclusão dos CSSs e JSs.
- Estrutura principal (`{% block %}` para herança dos outros templates).

### `home.html`
Extende `index.html` e apresenta:
- Um título de boas-vindas.
- Um parágrafo descritivo.
- Um botão estilizado que leva para a página de adição de projetos.

### `addprojeto.html`
Extende `index.html` e apresenta:
- Um formulário para criação de novos projetos.
- Input para imagem com sistema de arrastar e soltar (`drag and drop`).

### `lista_projetos.html`
Extende `index.html` e apresenta:
- Um card para cada projeto, mostrando:
  - Imagem.
  - Botões para editar e remover projetos.
  - Lista de tarefas.
  - Opção para adicionar nova tarefa por modal.

---

## 🎨 Estilização

- **Tailwind CSS**: usado para responsividade, alinhamento, gaps e espaçamento.
- **CSS personalizado** (`Homepage.css`):
  - Estiliza principalmente a homepage (cores de fundo, botões, tamanhos de fontes).
  - Define comportamento de hover em botões.

---

## 🛠 Tecnologias Usadas

- **Python 3** + **Flask**
- **HTML 5** + **Jinja2**
- **CSS 3** (Tailwind e manual)
- **Bootstrap 5** (para modais e componentes visuais)
- **JavaScript** (pré-visualização da imagem no formulário)

---

## ⚙️ Como Rodar Localmente

1. **Instalar dependências**:
   ```bash
   pip install Flask
2. **Iniciar o app**:
   ```bash
    python app.py
3. **Acessar no navegador**:
   ```bash
   http://localhost:5000

## Bootstrap

1. **Oque é Bootstrap**:
   O Bootstrap é um framework CSS criado para facilitar o desenvolvimento de sites responsivos (que funcionam bem no celular e no computador).
   Ele já vem com estilos prontos (botões, formulários, navbar, grid de layout etc.) e comportamentos prontos (como modal, carrossel, dropdowns) que você pode usar só adicionando classes específicas no HTML, sem       precisar criar tudo do zero.
  
2. **Como foi usado**:

   Utilizei o bootstrap principalmente para:
   - Layout (containers, grid)
   - Componentes (card, modal, botão, lista)
   - Utilitários (espaçamento, alinhamento)
