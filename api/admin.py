from django.contrib import admin
from .models import Book,User,Issued_Book

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Issued_Book)