from django.shortcuts import render

from blog.models import *

# Create your views here.



def blog(request):



    posts = post.objects.all()
    return render(request, 'blog/blog.html', {"posts": posts})


def categorias(request,categoria_id):

    categoriaz = categoria.objects.get(id = categoria_id)

    posts = post.objects.filter(categorias = categoriaz)
    return render(request, 'blog/categorias.html',{'categoria':categoriaz,"posts":posts})
