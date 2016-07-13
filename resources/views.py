from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse('Olá! Você criou sua primeira requisição.')
    context_return = {
        'course_name' : 'Python e Django na Prática',
        'alunos_list': [
            {'name' : 'Arthur'},
            {'name' : 'João'},
            {'name' : 'Maria'},
            {'name' : 'Pedro'},
            {'name' : 123456 },
        ],
    }
    return render(request,'hello.html',context_return)
