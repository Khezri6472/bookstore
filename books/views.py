from django.shortcuts import render
from django.views import generic

from books.models import Book


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book_detail'

