# app/views.py
from django.shortcuts import render
from .models import Usuario, Genero, Editora, Autor, Livro, Emprestimo, Cidade

def index(request):
    usuarios = Usuario.objects.all()
    generos = Genero.objects.all()
    editoras = Editora.objects.all()
    autores = Autor.objects.all()
    livros = Livro.objects.all()
    emprestimos = Emprestimo.objects.all()
    cidades = Cidade.objects.all()
    context = {
        'usuarios': usuarios,
        'generos': generos,
        'editoras': editoras,
        'autores': autores,
        'livros': livros,
        'emprestimos': emprestimos,
        'cidades': cidades,
    }
    return render(request, 'app/index.html', context)

def livros(request):
    
    livros = Livro.objects.all() 
    context = {'livros': livros}
    return render(request, 'app/livros.html', context)

def generos(request):
    
    generos = Genero.objects.all() 
    context = {'genero': generos}
    return render(request, 'app/genero.html', context)


def editoras(request):
    editoras = Editora.objects.all()  # Busca todas as editoras do banco de dados
    context = {'editor': editoras}  # Cria o contexto com o nome 'editor'
    return render(request, 'app/editor.html', context)


def cidades(request):
    
    cidade = Cidade.objects.all() 
    context = {'cidade': cidade}
    return render(request, 'app/cidades.html', context)

def autores(request):
    
    autores = Autor.objects.all() 
    context = {'Autores': autores}
    return render(request, 'app/autores.html', context)

def emprestimo(request):
    
    emprestimo = Emprestimo.objects.all() 
    context = {'emprestimo': emprestimo}
    return render(request, 'app/emprestimo.html', context)

def usuarios(request):
    
    usuarios = Usuario.objects.all() 
    context = {'usuarios': usuarios}
    return render(request, 'app/usuarios.html', context)
