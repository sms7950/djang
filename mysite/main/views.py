from django.shortcuts import render
# 모델에 post 가져오기
from .models import post


# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def blog(request):
    postlist = post.objects.all()
    return render(request, 'main/blog.html', {'postlist' :postlist})
#게시글별 세부페이지
def postdetails(request, pk):
    postlist = post.objects.get(pk=pk)
    return render(request, 'main/postdetails.html', {'postlist':postlist})

