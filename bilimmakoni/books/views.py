from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def home(request):
    return HttpResponse('<h1>Bilim Makoni</h1><a href="/books/">Kitoblar ro\'yxati</a>')
