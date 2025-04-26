from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Property
from .forms import PropertyForm, UserRegistrationForm

def property_list(request):
    properties = Property.objects.all()
    paginator = Paginator(properties, 9)  # 9 properties per page
    page = request.GET.get('page')
    properties = paginator.get_page(page)
    return render(request, 'listings/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property})

@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user
            property.save()
            messages.success(request, 'Votre annonce a été publiée avec succès !')
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm()
    return render(request, 'listings/property_form.html', {'form': form, 'title': 'Ajouter une propriété'})

@login_required
def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if property.owner != request.user:
        messages.error(request, 'Vous n\'êtes pas autorisé à modifier cette annonce.')
        return redirect('property_list')
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            property = form.save()
            messages.success(request, 'Votre annonce a été mise à jour avec succès !')
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'listings/property_form.html', {'form': form, 'title': 'Modifier la propriété'})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Votre compte a été créé avec succès !')
            return redirect('property_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'listings/register.html', {'form': form})
