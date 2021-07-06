from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article, Images


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photos_of_day(request):
    date = dt.date.today()
    photos = Article.todays_photos()
    return render(request, 'all-photos/today-photos.html', {"date": date,"photos":photos})

def past_days_photos(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    photos = Article.days_photos(date)
    return render(request, 'all-photos/past-photos.html', {"date": date,"photos":photos})

def search_results(request):
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except ValueError:
        raise Http404()
    return render(request,"all-photos/article.html", {"article":article}) 

def image(request,images_id):
    try:
        image = Images.objects.get(id = images_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photo/artilce.html", {"image":image})
def filter_by_location(request,location_id):
   """
   Function that filters images by location
   """
   images = Images.filter_by_location(id=location_id )
   return render (request, 'location.html', {"images":images})
   