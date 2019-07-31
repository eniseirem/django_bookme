from django.shortcuts import render
import requests

import json
# Create your views here.



def homepage(request):
    response = requests.get('https://api.itbook.store/1.0/new')
    bookdata = response.json()
    bookinfo = bookdata['books']
    b_range = int(bookdata['total'])

    return render(request, 'homepage.html', { 'bookdata': bookdata, 'bookinfo': bookinfo, 'range' : range(b_range) })
def booklist(request):
    return render(request, 'booklist.html')

def booksdetails(request):
    return render(request, 'booksdetails.html')
