from django.shortcuts import render, get_object_or_404
from datetime import datetime

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def book_date_view(request, date):
    datetime_date = datetime.strptime(date, '%Y-%m-%d')
    current_book = get_object_or_404(Book, pub_date=datetime_date)

    context = {
        "book": current_book,
    }

    return render(request, 'books/book.html', context)