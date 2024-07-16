from django.shortcuts import render, get_object_or_404, redirect
from .models import CONTACT
from .forms import Contacts

def Contact(request):
    contacts = CONTACT.objects.all() 
    return render(request, 'index.html', {'contacts':contacts})

def AddContact(request): 
    if request.method == 'POST': 
        form = Contacts(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('index')
    else: 
        form = Contacts()
    return render(request, 'update.html', {'form':form})

def SearchContact(request): 
    query = request.GET.get('query')
    results = CONTACT.objects.filter(name__icontains = query) | CONTACT.objects.filter(phone__icontains=query)
    return render(request, 'search.html', {'contacts': results, 'query' : query})

def UpdateContact(request,pk):
    contact = get_object_or_404(CONTACT, pk=pk)
    if request.method == 'POST': 
        form = Contacts(request.POST, instance=contact)
        if form.is_valid(): 
            form.save()
            return redirect('index')
    else: 
        form = Contacts(instance=contact)
    return render(request, 'update.html',{'form': form})

def DeleteContact(request,pk):
    contact = get_object_or_404(CONTACT, pk=pk)
    if request.method == 'POST': 
        contact.delete()
        return redirect('index')
    return render(request, 'delete.html',{'contact': contact})

