from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Education
from .models import Work_Experience
from .models import Personal_Statement
from .models import *

# Create your views here.

def index(request):
    top_post = Post.objects.order_by('-total_views').first()
    most_recent = Post.objects.order_by('-published_date').first()
    return render(request, 'blog/index.html', {'top_post':top_post, 'most_recent':most_recent})
    
def introduction(request):
    education = Education.objects.all()
    work_experience = Work_Experience.objects.all()
    ps = Personal_Statement.objects.all()
    year1 = UoB_Year_1.objects.all()
    year2 = UoB_Year_2.objects.all()
    year3 = UoB_Year_3.objects.all()
    details = MyDetail.objects.all()
    return render(request, 'blog/introduction.html', {'education':education, 'work_experience':work_experience, 'ps':ps, 'year1':year1,'year2':year2,'year3':year3,'details':details})
    
def daily(request):
    albums = Gallery.objects.all()
    return render(request, 'blog/daily.html', {'albums':albums})
    
def daily_detail(request, pk, album_name):
    album = get_object_or_404(Gallery, pk=pk)
    photos = Photos.objects.filter(album_name=pk)
    return render(request, 'blog/daily_detail.html',{'album':album, 'photos':photos})
    
def photo(request, pk):
    photoPK = Photos.objects.get(pk=pk)
    return render(request, 'blog/photo.html', {'photoPK':photoPK})

def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts':posts})
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.total_views += 1
    post.save(update_fields=['total_views'])
    return render(request, 'blog/post_detail.html',{'post':post})
