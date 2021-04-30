from django.shortcuts import render
from .models import Post
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

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


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request, 'home/register.html', {"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'home/login.html', context={"login_form":form})