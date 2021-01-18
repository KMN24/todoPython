from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo, BookShop


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list}) # в test.html отпавляется "todo_list"

def second(request):
    return HttpResponse("test2 page")

def bookShop(request):
    book_shop = BookShop.objects.all()
    return render(request, "books.html", { "book_shop": book_shop })

def add_bookshop(request):
    form = request.POST
    title = form["bookshop_title"]
    subtitle = form["bookshop_subtitle"]
    description = form["bookshop_description"]
    price = form["bookshop_price"]
    genre = form["bookshop_genre"]
    author = form["bookshop_author"]
    year = form["bookshop_year"]
    bookshop = BookShop(
        title = title, 
        subtitle = subtitle,
        description = description,
        price = price,
        genre = genre,
        author = author,
        year = year
        )
    bookshop.save()
    return redirect(bookShop)

def add_todo(request):
    form = request.POST 
    text = form["todo_text"]
    #print(text)
    todo= ToDo(text=text) # 1 text - это тот который в models.py
    todo.save()
    return redirect(test) # обратно вернемся к странице test.html
    # здесь test это функция