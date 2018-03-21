from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,'index.html') 
def contato(request):
	return render(request,'contato.html')
def login(request):
	if request.POST.get("senhauser")=='teste123':
		print ("Usuário",request.POST.get("nomeuser"),"Entrou com sucesso No Sistema")
		return render(request,'index.html')
	else:
		print ("Usuário",request.POST.get("nomeuser"),"acesso negado")
	return render(request,'login.html')
	