from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, DetailView
from django.urls import reverse, reverse_lazy
from .models import Book
from .forms import BookForm

# Create your views here.
class IndexView(ListView):
    template_name = 'shop/index.html'
    context_object_name = 'books'
    model = Book

index = IndexView.as_view()


class DetailView(DetailView):
    model = Book
    template_name = 'shop/detail.html'
    context_object_name = 'book'
    slug_field = 'id'
    slug_url_kwarg = 'book_id'

detail = DetailView.as_view()


class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'shop/add_book.html'
    success_url = reverse_lazy('shop:index')

add_book = AddBookView.as_view()
