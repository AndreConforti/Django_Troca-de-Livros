from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    # recebe o valor enviado pela URL da variável de acordo com a validação
    # feita na função valida_cadastro()
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status,})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(senha.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    if len(senha.strip()) < 4:
        return redirect('/auth/cadastro/?status=2')
    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    try:
        # Conserve a senha do usuário em um conjunto de caracteres hexadecimais
        # de tamanho 64, independetemente do tamanho da senha que o usuário digitar.
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(
            nome=nome,
            email=email,
            senha=senha,
        )
        usuario.save()
        # Cria uma variável de nome 'status' que vai armazenar o valor de acordo com 
        # o erro ou validação que for feita
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')