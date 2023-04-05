from django.db import models


class Categoria(models.Model):
    """Classe para definir o cadastro das categorias referentes aos livros do usuário logado."""
    nome = models.CharField(max_length=50)
    descricao = models.TextField()


class Livro(models.Model):
    """Classe para cadastro de livros do usuário que estiver logado."""
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    co_autor = models.CharField(max_length=50, null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=50, null=True, blank=True)
    data_emprestimo = models.DateField(null=True,blank=True)
    data_devolucao = models.DateField(null=True, blank=True)

    class Meta:
        """Essa classe configura um método na área de Admin do Django,
            onde o nome da classe aparece no plural. Porém se já houve um 's' no final,
            na área Admin vai aparecer com 'ss'. Utiliza a classe na forma verbal."""
        verbose_name = 'Livro'
    
    def __str__(self):
        return self.nome
