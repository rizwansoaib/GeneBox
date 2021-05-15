from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def sayname(request,name):

    return render(request,'name.html',{'name':name})


def add_author(request):
    authorform=AuthorForm()
    bookform=BookForm()
    if request.method=='POST':
        add_author_form=AuthorForm(request.POST)
        if add_author_form.is_valid():
            add_author_form.save()

        add_book_form=BookForm(request.POST)
        if add_book_form.is_valid():
            add_book_form.save()
    query=Books.objects.all()
    context={
        'authorform':authorform,
        'bookform':bookform,
        'books':query
    }
    return render(request,'forms.html',context)


