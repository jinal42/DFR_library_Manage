from django.db import models

from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# # from .managers import UserManager 
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import BaseUserManager

from datetime import datetime,timedelta,date



class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff,
                     is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        user = self.model(email=self.normalize_email(email),
                          is_active=True,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_user(self, email=None, password=None, **extra_fields):
        is_staff = extra_fields.pop('is_staff', False)
        is_superuser = extra_fields.pop('is_superuser', False)
        return self._create_user(email, password, is_staff,
                                 is_superuser, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, is_staff=True,
                                 is_superuser=True, **extra_fields)

user_type=[('student','Student'),('librarian','Librarian')]

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    user_name=models.CharField(('user_name'),unique=True,max_length=30)
    # Customer_Type=models.ForeignKey(Customer_Type, on_delete = models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('is_staff'), default=True)
    user_type=models.CharField(('user_type'),choices=user_type,max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str__(self):
        return self.user_name



class Book(models.Model): 
    book_title=models.CharField(unique=True,max_length=150)
    book_author=models.CharField(max_length=30)

    def __str__(self):
        return self.book_title

def expiry():
        return date.today() + timedelta(days=7)


class Issued_Book(models.Model):

    
    # Borrower_id=models.IntegerField(unique=True)
    book_id=models.ForeignKey(Book,on_delete = models.CASCADE,null=True,blank=True)
    user_id=models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
    issue_date=models.DateField(auto_now=True)
    # issue_date=models.DateField(default=date.today)

    return_date=models.DateField(default=expiry)
    actual_return_date=models.DateField(null=True,blank=True)
    fine=models.IntegerField(default=0)

    




