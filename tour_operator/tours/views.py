from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tour
from .forms import TourForm

@login_required
def tour_list(request):
    tours = Tour.objects.select_related('country', 'hotel').all()
    return render(request, 'tours/list.html', {'tours': tours})


@login_required
def tour_create(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            tour = form.save()
            messages.success(request, f'Тур {tour.name} успешно добавлен')
            return redirect('tours:list')
    else:
        form = TourForm()

    return render(request, 'tours/form.html', {'form': form})


@login_required
def tour_update(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'POST':
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            messages.success(request, f'Тур {tour.name} успешно обновлен')
            return redirect('tours:list')
    else:
        form = TourForm(instance=tour)
    return render(request, 'tours/form.html', {'form': form})


@login_required
def tour_delete(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'POST':
        tour.delete()
        messages.success(request, f'Тур {tour.name} успешно удален')
        return redirect('tours:list')
    return render(request, 'tours/delete.html', {'tour': tour})