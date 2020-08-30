from django.shortcuts import render

from .models import Contact
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = Contact(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                content=form.cleaned_data["content"]
                )
            new_contact.save()
    else:
        form = ContactForm()
    return render(request, 'contact.html', context={"form": form})
