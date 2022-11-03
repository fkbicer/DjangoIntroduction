from learning.forms import Contact
from django.shortcuts import render
from django.http import HttpResponseRedirect


def contact_form(request):

    if request.method == "POST":
        form = Contact(request.POST) # form degiskenine POST gelir ise atama yapıyoruz.
        if form.is_valid(): #validasyonlardan geçtiğine dair method. cleaned_data ile bu verileri çekebiliriz.
            subject = form.cleaned_data['name']
            message = form.cleaned_data['content']
            sender = form.cleaned_data['email']

        return HttpResponseRedirect('/') # islem sonunda buraya redirect ederiz.
    else:
        form = Contact()

    return render(request=request, template_name='contact/form.html', context={'form': form})
