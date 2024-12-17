from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client
from .forms import ClientForm

# Клиенты
@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/list.html', {'clients': clients})


@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            messages.success(request, f'Клиент {client} успешно добавлен')
            return redirect('clients:list')
    else:
        form = ClientForm()

    return render(request, 'clients/form.html', {'form': form})


@login_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, f'Клиент {client} успешно обновлен')
            return redirect('clients:list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/form.html', {'form': form})


@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, f'Клиент {client} успешно удален')
        return redirect('clients:list')
    return render(request, 'clients/delete.html', {'client': client})