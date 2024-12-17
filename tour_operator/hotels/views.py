from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Hotel
from .forms import HotelForm

@login_required
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/list.html', {'hotels': hotels})


@login_required
def hotel_create(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel = form.save()
            messages.success(request, f'Отель {hotel.name} успешно добавлен')
            return redirect('hotels:list')
    else:
        form = HotelForm()

    return render(request, 'hotels/form.html', {'form': form})


@login_required
def hotel_update(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, f'Отель {hotel.name} успешно обновлен')
            return redirect('hotels:list')
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hotels/form.html', {'form': form})


@login_required
def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        messages.success(request, f'Отель {hotel.name} успешно удален')
        return redirect('hotels:list')
    return render(request, 'hotels/delete.html', {'hotel': hotel})