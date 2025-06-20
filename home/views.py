from django.shortcuts import render, redirect
from .models import Books
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required 

# Create your views here.
@login_required
def index(request):
    all_books = Books.objects.all()
    return render(request, 'main/books_display.html',
                  context={
                      'books': all_books
                  })

@login_required
def book_details(request, pk):
    book = Books.objects.get(pk=pk)
    return render(request, 'main/book_details.html', context={'book':book})

@login_required
def book_delete(request, pk):
    Books.objects.get(pk=pk).delete()
    return redirect('home:home')

@login_required
@permission_required('home.add_books', raise_exception=True)
def book_create(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
        
    return render(request,'main/book_create.html',
                  context={
                      'form': form
                  })

@login_required
def book_update(request, pk):
    book = Books.objects.get(pk=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(instance=book,data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("home:home")
    return render(request, "main/book_update.html", context={
        "form": form,
        "book": book
    })