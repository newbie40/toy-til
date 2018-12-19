# Create your views here.
from django.shortcuts import render

from .models import Post, Category


def index(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()

    context = {'post_list': post_list, 'category_list': category_list}
    return render(request, 'til/index.html', context)
