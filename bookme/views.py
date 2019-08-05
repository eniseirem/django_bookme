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

#checking the booklist for duplicate
    obj, created = Booklist.objects.get_or_create(isbn13=id, defaults={'title': name, 'image': img})
    next = request.POST.get('next', request.GET.get('back'))

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
        bookinfo = []
        total = int(bookdata['total'])


#takes the all results from api and add them to a list for later use
        if total%10 is 0:
            page_b = total//10
        else:
            page_b = (total//10)+1
        for i in range(1,page_b+1):
            p = str(i)
            response = requests.get('https://api.itbook.store/1.0/search/' + search_term+'/'+p)
            bookdata_p = response.json()

            for item in bookdata_p['books']:
                bookinfo.append(item)




#paginator
    paged_bookinfo=list(request,bookinfo)

#keeping params for paginator
    params = request.GET.get('search', '')
    params_link="search="+params

    return render(request, 'homepage.html', {'bookinfo': paged_bookinfo, 'params':params_link})

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

