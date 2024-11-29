from django.shortcuts import render
from .models import Book, Author, Customer

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'books/author_list.html', {'authors': authors})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'books/customer_list.html', {'customers': customers})

def index(request):
    return render(request, 'books/index.html')
