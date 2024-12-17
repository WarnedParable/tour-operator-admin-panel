from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Country
from .forms import CountryForm

@login_required
def country_list(request):
    countries = Country.objects.all()
    return render(request, 'countries/list.html', {'countries': countries})


@login_required
def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            try:
                # Явное сохранение формы
                country = form.save()
                # Добавим сообщение об успехе
                messages.success(request, f'Страна {country.name} успешно добавлена')
                return redirect('countries:list')
            except Exception as e:
                # Логирование ошибки
                messages.error(request, f'Ошибка при сохранении: {str(e)}')
    else:
        form = CountryForm()

    return render(request, 'countries/form.html', {'form': form})

@login_required
def country_update(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('countries:list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'countries/form.html', {'form': form})

@login_required
def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
        return redirect('countries:list')
    return render(request, 'countries/delete.html', {'country': country})