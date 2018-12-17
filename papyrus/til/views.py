# Create your views here.
from django.shortcuts import render

from .models import Post


def index(request):
    post_list = Post.objects.all()
    return render(request, 'til/index.html', {'post_list': post_list})

