from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from openpyxl import Workbook
from django.shortcuts import redirect
from countries.models import Country
from clients.models import Client
from contracts.models import Contract
from hotels.models import Hotel
from tours.models import Tour


@login_required
def dashboard(request):
    user = request.user
    is_admin = user.is_admin

    sections = [
        {'name': 'Страны', 'url': 'countries:list', 'admin_only': True},
        {'name': 'Сотрудники', 'url': 'accounts:employee_list', 'admin_only': True},
        {'name': 'Отели', 'url': 'hotels:list', 'admin_only': True},
        {'name': 'Туры', 'url': 'tours:list', 'admin_only': True},
        {'name': 'Клиенты', 'url': 'clients:list', 'admin_only': False},
        {'name': 'Контракты', 'url': 'contracts:list', 'admin_only': False},
    ]

    available_sections = [
        section for section in sections
        if not section['admin_only'] or (section['admin_only'] and is_admin)
    ]

    context = {
        'sections': available_sections,
        'is_admin': is_admin,
        'username': user.username
    }

    return render(request, 'dashboard/dashboard.html', context)

@login_required
def export_data(request):
    tables = {
        'countries': Country.objects.all(),
        'clients': Client.objects.all(),
        'contracts': Contract.objects.all(),
        'hotels': Hotel.objects.all(),
        'tours': Tour.objects.all(),
    }

    if request.method == 'POST':
        table_name = request.POST.get('table')
        export_format = request.POST.get('format')

        if table_name not in tables or export_format not in ['json', 'xlsx']:
            return redirect('dashboard:export_data')

        queryset = tables[table_name]

        if export_format == 'json':
            data = list(queryset.values())
            response = JsonResponse(data, safe=False)
            response['Content-Disposition'] = f'attachment; filename={table_name}.json'
            return response

        if export_format == 'xlsx':
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = table_name.capitalize()

            fields = [field.name for field in queryset.model._meta.fields]
            sheet.append(fields)

            for obj in queryset:
                sheet.append([getattr(obj, field) for field in fields])

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={table_name}.xlsx'
            workbook.save(response)
            return response

    return render(request, 'dashboard/export.html', {'tables': tables.keys()})