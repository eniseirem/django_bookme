from django.shortcuts import render
import requests
from django.shortcuts import redirect
from .models import Booklist
import logging
from django.http import HttpResponseRedirect
import json
# Create your views here.


from django.contrib import messages

def add_list(request, id, name, img):
    #need to use sessions for id

    obj, created = Booklist.objects.get_or_create(isbn13=id, defaults={'title': name, 'image': img})
    if created is False:
        return homepage(request)

    else:

        return booklist(request)


# #add here to add to list
#    messages.info(request, 'Book saved to your list successfully!')
#    return HttpResponseRedirect('.')

def homepage(request):
    response = requests.get('https://api.itbook.store/1.0/new')
    bookdata = response.json()
    bookinfo = bookdata['books']
    b_range = int(bookdata['total'])

    return render(request, 'homepage.html', {'bookdata': bookdata, 'bookinfo': bookinfo, 'range': range(b_range)})
def booklist(request):

    bookinfo = Booklist.objects.all()
    b_range = Booklist.objects.count()
    return render(request, 'booklist.html', {'bookinfo': bookinfo, 'range': range(b_range)})

def booksdetails(request,id):
    id_s = str(id)
    response = requests.get('https://api.itbook.store/1.0/books/'+id_s)

    bookdata = response.json()
    bookinfo = {}
    bookinfo[0] = bookdata
    b_range = 1
    return render(request, 'booksdetails.html',{'bookinfo': bookinfo, 'range': range(b_range)})
