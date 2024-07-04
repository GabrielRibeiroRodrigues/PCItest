from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    datadenascimento = 
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome

class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome    

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(blank=True, null=True)
    telefone = models.CharField(max_lenght = 11) 
    cidade = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Area(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    cargahoraria = models.CharField(max_lenght = 10)
    duracao = models.CharField(max_lenght = 10)

    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    nome = models.CharField(max_lenght = 30)
    
    def __str__(self):
        return f'{self.livro} emprestado por {self.leitor}'

class Matricula(models.Model):
    data_inicio= models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100)
    
class Frequencia(models.Model):
    numero_faltas = models.CharField(max_length=100)
     

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

class Ocorrencias(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

class Tipo_Avaliacao(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)      