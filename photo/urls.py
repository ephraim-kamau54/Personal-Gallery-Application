from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.photos_of_day,name='home'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos'), 
    url(r'^search/', views.search_results, name='search_results'), 
    url(r'^article/(\d+)',views.article,name ='article'),
    url(r'^location/(\d+)',views.filter_by_location,name='location'),
    url(r'^gallery/',views.gallery,name='gallery'),
    url(r'^photo/(\d+)',views.viewPhoto,name ='photo')
]
