from django.shortcuts import render

from .models import post
# 모델에 post 가져오기

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def blog(request):
    postlist = post.objects.all()
    return render(request, 'main/blog.html', {'postlist' :postlist})

