from django.shortcuts import render
import requests
from django.shortcuts import redirect
from bookme.models import Booklist
from django.core.paginator import Paginator
import logging
from django.http import HttpResponseRedirect
import json
# Create your views here.

from django.contrib import messages

def add_list(request, id, name, img):

    obj, created = Booklist.objects.get_or_create(isbn13=id, defaults={'title': name, 'image': img})
    next = request.POST.get('next', '/')

    if created is False:
        messages.error(request, 'Book already exist in your list')


    else:
        messages.success(request, 'Book saved to your list successfully!')

    return HttpResponseRedirect(next)


def homepage(request):
    response = requests.get('https://api.itbook.store/1.0/new')
    bookdata = response.json()
    bookinfo = bookdata['books']

    if 'search' in request.GET:
        search_term = request.GET['search']
        response = requests.get('https://api.itbook.store/1.0/search/'+search_term)
        bookdata = response.json()
        bookinfo = bookdata['books']
        total = int(bookdata['total'])
        b_range = len(bookinfo)

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



        if b_range == 0:
            messages.info(request, 'Could not find any match. Try something else')



    paged_bookinfo=list(request,bookinfo)



    return render(request, 'homepage.html', {'bookinfo': paged_bookinfo},)

def booklist(request):

    bookinfo = Booklist.objects.all()
    paged_bookinfo=list(request,bookinfo)

    return render(request, 'booklist.html', {'bookinfo': paged_bookinfo})

def booksdetails(request,id):
    id_s = str(id)
    response = requests.get('https://api.itbook.store/1.0/books/'+id_s)

    bookdata = response.json()
    bookinfo = []
    bookinfo.append(bookdata)
    paged_bookinfo = list(request, bookinfo)

    return render(request, 'booksdetails.html',{'bookinfo': paged_bookinfo})

def list(request,pagine):
    paginator = Paginator(pagine,10)
    page = request.GET.get('page')
    pagine = paginator.get_page(page)
    return pagine

