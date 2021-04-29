from django.shortcuts import render
from .models import Post

# dummy data
# posts = [
#   {
#     'author': 'Franklin',
#     'title': 'Post 1',
#     'description': 'first posts',
#     'dated_posted': 'August 27, 2020'
#   },
#   {
#     'author': 'Jose',
#     'title': 'Post 2',
#     'description': 'second posts',
#     'dated_posted': 'June 8, 2020'
#   }
# ]

# Create your views here.
def index(request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'home/index.html', context)

# localhost:3000/aboutUs
def aboutUs(request):
  return render(request, 'home/aboutUs.html')