from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contract
from .forms import ContractForm

@login_required
def contract_list(request):
    contracts = Contract.objects.select_related('tour', 'client').all()
    return render(request, 'contracts/list.html', {'contracts': contracts})


@login_required
def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save()
            messages.success(request, f'Договор {contract.id} успешно создан')
            return redirect('contracts:list')
    else:
        form = ContractForm()

    return render(request, 'contracts/form.html', {'form': form})


@login_required
def contract_delete(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        contract.delete()
        messages.success(request, f'Договор {contract.id} успешно удален')
        return redirect('contracts:list')
    return render(request, 'contracts/delete.html', {'contract': contract})
