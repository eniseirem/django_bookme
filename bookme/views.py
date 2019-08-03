from django.shortcuts import render
import requests
from django.shortcuts import redirect
from .models import Booklist
from django.core.paginator import Paginator
import logging
from django.http import HttpResponseRedirect
import json
# Create your views here.

from django.contrib import messages

def add_list(request, id, name, img):

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
    b_range = len(bookinfo)
    if 'search' in request.GET:
        search_term = request.GET['search']
        response = requests.get('https://api.itbook.store/1.0/search/'+search_term)
        bookdata = response.json()
        bookinfo = bookdata['books']
        total = int(bookdata['total'])
        if total%2 is 0:
            page_b = total//10
        else:
            page_b = (total//10)+1
        for i in range(page_b):
            p = str(i)
            response = requests.get('https://api.itbook.store/1.0/search/' + search_term+'/'+p)
            bookdata = response.json()
            total_b = len(bookdata['books'])
            for x in range(total_b):
                bookinfo.append(bookdata['books'][x])


        b_range = len(bookinfo)

        if b_range == 0:
            return booklist(request)


    # paginator = list(bookinfo)
    # page = request.GET.get('page')
    # bookinfo = paginator.get_page(page)
    return render(request, 'homepage.html', {'bookinfo': bookinfo, 'range': range(b_range)})

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

def list(pagine):
    paginator = Paginator(pagine,10)
    return paginator

def lookup(d, key):
    return d[key]