from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import EmployeeCreationForm
from .models import CustomUser


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('dashboard:home')
        else:
            messages.error(request, 'Неверный логин или пароль')

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы')
    return redirect('accounts:login')


def is_admin(user):

    return user.is_admin


@login_required
@user_passes_test(is_admin)
def employee_list(request):

    employees = CustomUser.objects.filter(user_type='regular')
    return render(request, 'accounts/employee_list.html', {'employees': employees})


@login_required
@user_passes_test(is_admin)
def employee_create(request):

    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            try:
                employee = form.save()
                messages.success(request, f'Работник {employee.username} успешно создан')
                return redirect('accounts:employee_list')
            except Exception as e:
                messages.error(request, f'Ошибка при создании работника: {str(e)}')
                import traceback
                traceback.print_exc()
    else:
        form = EmployeeCreationForm()

    return render(request, 'accounts/employee_create.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def employee_delete(request, pk):
    employee = get_object_or_404(CustomUser, pk=pk, user_type='regular', is_admin=False)

    if request.method == 'POST':
        try:
            employee.delete()
            messages.success(request, f'Работник {employee.username} удален')
            return redirect('accounts:employee_list')
        except Exception as e:
            messages.error(request, f'Ошибка при удалении: {str(e)}')

    return render(request, 'accounts/employee_delete.html', {'employee': employee})
