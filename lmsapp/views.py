from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, BookForm
from .models import Book
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def index(request):
    return render(request, 'index.html', {'title': 'index'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'reqister here'})


def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


@login_required()
def view_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books, 'title': 'View all books'})


@login_required()
def create_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST) or None
        if book_form.is_valid():
            book_form.save()
            messages.success(request, f' New book created !!')
            return redirect('index')
        else:
            messages.info(request, f'Something went wrong in book creation')

    book_form = BookForm()
    return render(request, 'create_book.html', {'form': book_form, 'title': 'Create Book'})
