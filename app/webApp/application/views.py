from django.shortcuts import render
from .models import Reporter, Article 
from django.utils import timezone

# Create your views here.
# localhost:3000/index

def index(request):
  reporter1 = Reporter(full_name='Begum')
  artical1 = Article(headline='test_headline', content='testtt', pub_date=timezone.now())
  reporter1.save()
  artical1.save()
  return render(request, 'home/index.html')

# localhost:3000/aboutUs
def aboutUs(request):
  return render(request, 'home/aboutUs.html')
  

  
  
  
  
