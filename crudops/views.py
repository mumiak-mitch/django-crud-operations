from django.shortcuts import render, redirect
from .forms import LanguageForm
from .models import Programming

def crud_list(request):
    context = {'crud_list': Programming.objects.all()}
    return render(request, 'crudops/crudlist.html', context)

def crud_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = LanguageForm()
        else:
            programming = Programming.objects.get(pk=id)
            form = LanguageForm(instance=programming)
        return render(request, 'crudops/crudform.html', {'form': form})
    else:
        if id == 0:
            form = LanguageForm(request.POST)
        else:
            programming = Programming.objects.get(pk=id)
            form = LanguageForm(request.POST, instance=programming)
        if form.is_valid():
            form.save()
        return redirect('crudlist')

def crud_delete(request, id):
    programming = Programming.objects.get(pk=id)
    programming.delete()
    return redirect('crudlist')