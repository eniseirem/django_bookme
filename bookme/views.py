from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
import json
# Create your views here.


from django.contrib import messages

def add_list(request):

#add here to add to list 
   messages.info(request, 'Book saved to your list successfully!')
   return HttpResponseRedirect('.')

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
