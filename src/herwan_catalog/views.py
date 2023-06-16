from django.shortcuts import render, redirect
from .models import Planeta
from .forms import PlanetaForm

def home(request):
    return render(request, 'home.html', {})

def novo_planeta(request):
    if request.method == 'POST':
        form = PlanetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlanetaForm()
    
    context = {'form': form}
    return render(request, 'novo_planeta.html', context)

def salvar_planeta(request):
    if request.method == 'POST':
        form = PlanetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlanetaForm()
    
    context = {'form': form}
    return render(request, 'novo_planeta.html', context)