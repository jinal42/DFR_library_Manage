# https://django-book.readthedocs.io/en/latest/chapter10.html

from django.contrib import admin
from django.urls import path,include

from api.views import UserAPI,LoginAPI,UserDetail
from api.views import BookAPI,Search_Book,Searchh,Issued_BookAPI,FineAPI

# from .views import SeaList

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/',include('rest_framework.urls')),

    path('user/',UserAPI.as_view()),
    path('user/<int:id>/',UserAPI.as_view()),

    path('login/',LoginAPI.as_view()),

    path('book/',BookAPI.as_view()),
    path('book/<int:id>/',BookAPI.as_view()),

    path('book-search/',Search_Book.as_view()),
    path('searchh/',Searchh.as_view()),

    path('info/',UserDetail.as_view()),
    path('info/<int:id>/',UserDetail.as_view()),


    path('issue/',Issued_BookAPI.as_view()),
    path('issue/<int:id>/',Issued_BookAPI.as_view()),

  
    path('fine/',FineAPI.as_view()),
    path('fine/<int:id>/',FineAPI.as_view()),


]   
