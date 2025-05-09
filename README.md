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
<img width="947" alt="Captura de tela 2025-05-09 081233" src="https://github.com/user-attachments/assets/60d18a88-3138-4661-8a3a-27aaad439285" />

- Na Home page do projeto fiz uma NAV com botões "HOME" "ADICIONAR PROJETO" "LISTAGEM" onde direciona o usuario para as paginas destintas, abaixo coloquei um titulo e um paragrafo para estilizar a tela e ambientar em conjunto d eum botão de "ADICIONAR PROJETO" caso o usuario queira usar o botão para ir a pagina de add projeto

### `addprojeto.html`
Extende `index.html` e apresenta:
- Um formulário para criação de novos projetos.
- Input para imagem com sistema de arrastar e soltar (`drag and drop`).
  <img width="950" alt="Captura de tela 2025-05-09 081335" src="https://github.com/user-attachments/assets/ac2e1039-67b1-4c68-b848-f99d784912ee" />

- Na Pagina ADD PROJETO adicionei 2 campos de escrita onde vai o titulo do projeto e a descrição e abaixo um campo de upload de imagem para o usuario add uma imagem ao seus projetos, e no fim da pagina um botão de "ADD TAREFA" que faz o projeto ser adicionado, logo apos o usuario ja é direcionado para pagina LISTAGEM

### `lista_projetos.html`
Extende `index.html` e apresenta:
- Um card para cada projeto, mostrando:
  - Imagem.
  - Botões para editar e remover projetos.
  - Lista de tarefas.
  - Opção para adicionar nova tarefa por modal.
<img width="960" alt="Captura de tela 2025-05-09 081415" src="https://github.com/user-attachments/assets/dfc9bacf-be0c-4206-9311-b37fe8bf0cf8" />

- Na pagina listagem tem a imagem adicionado pelo usario, titulo e descrição do projeto, botão para editar e remover PROJETO. Abaixo fica um campo onde ficam amarzenada as tarefas do projeto, e abaixo do campo um botão de ADD TAREFA, quando a tarefa é adicionada ela aparece no campo junto do seu titulo e descrição, e do lado direito da tarefa um botão de remover a tarefa.
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
