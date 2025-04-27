
from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'sua_chave_secreta'  # chave necessária para usar flash
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

PROJECTS_CSV = 'projects.csv'
TASKS_CSV = 'tasks.csv'

def read_projects():
    projects = []
    if os.path.exists(PROJECTS_CSV):
        with open(PROJECTS_CSV, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                projects.append(row)
    return projects

def write_projects(projects):
    with open(PROJECTS_CSV, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'titulo', 'descricao', 'imagem']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(projects)

def read_tasks():
    tasks = []
    if os.path.exists(TASKS_CSV):
        with open(TASKS_CSV, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(row)
    return tasks

def write_tasks(tasks):
    with open(TASKS_CSV, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'projeto_id', 'titulo', 'descricao']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projetos')
def listar_projetos():
    projects = read_projects()
    tasks = read_tasks()
    for project in projects:
        project['tasks'] = [task for task in tasks if int(task['projeto_id']) == int(project['id'])]
    return render_template('lista_projetos.html', projects=projects)

@app.route('/addprojeto', methods=['GET', 'POST'])
def add_projeto():
    if request.method == 'POST':
        projects = read_projects()
        new_id = max([int(p['id']) for p in projects], default=0) + 1
        titulo = request.form['titulo']
        descricao = request.form['descricao']

        imagem = request.files.get('imagem')
        if imagem and imagem.filename != '':
            img_filename = imagem.filename
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
            imagem.save(img_path)
        else:
            img_filename = 'padrao.png'

        projects.append({'id': new_id, 'titulo': titulo, 'descricao': descricao, 'imagem': img_filename})
        write_projects(projects)

        flash('Projeto adicionado com sucesso!', 'success')
        return redirect(url_for('listar_projetos'))
    return render_template('add_projeto.html')

@app.route('/addtarefa/<int:projeto_id>', methods=['POST'])
def add_tarefa(projeto_id):
    tasks = read_tasks()
    new_id = max([int(t['id']) for t in tasks], default=0) + 1
    titulo = request.form['titulo']
    descricao = request.form['descricao']

    tasks.append({'id': new_id, 'projeto_id': projeto_id, 'titulo': titulo, 'descricao': descricao})
    write_tasks(tasks)

    flash('Tarefa adicionada com sucesso!', 'success')
    return redirect(url_for('listar_projetos'))

@app.route('/removerprojeto/<int:projeto_id>')
def remover_projeto(projeto_id):
    projects = read_projects()
    projects = [p for p in projects if int(p['id']) != projeto_id]
    write_projects(projects)

    tasks = read_tasks()
    tasks = [t for t in tasks if int(t['projeto_id']) != projeto_id]
    write_tasks(tasks)

    flash('Projeto removido com sucesso!', 'danger')
    return redirect(url_for('listar_projetos'))

@app.route('/removertarefa/<int:task_id>/<int:projeto_id>')
def remover_tarefa(task_id, projeto_id):
    tasks = read_tasks()
    tasks = [t for t in tasks if int(t['id']) != task_id]
    write_tasks(tasks)

    flash('Tarefa removida com sucesso!', 'danger')
    return redirect(url_for('listar_projetos'))

@app.route('/editarprojeto/<int:projeto_id>', methods=['POST'])
def editar_projeto(projeto_id):
    projects = read_projects()
    for project in projects:
        if int(project['id']) == projeto_id:
            project['titulo'] = request.form['titulo']
            project['descricao'] = request.form['descricao']

            imagem = request.files.get('imagem')
            if imagem and imagem.filename != '':
                img_filename = imagem.filename
                img_path = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
                imagem.save(img_path)
                project['imagem'] = img_filename
            break

    write_projects(projects)
    flash('Projeto editado com sucesso!', 'info')
    return redirect(url_for('listar_projetos'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
