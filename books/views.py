from django.urls import reverse_lazy
from django.views import generic


from .models import Book

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book_detail'
    template_name = 'books/book_detail.html'

class BookCreateView(generic.CreateView):
    model =Book
    fields = ['title', 'author', 'description','price']
    template_name = 'books/book_create.html'

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description','price']
    template_name = 'books/book_Update.html'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')




