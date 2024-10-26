from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a user name')
        if not password:
            raise ValueError('User must have a password')
        
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username=username, password=password, **extra_fields)
        
        ##user= self.create_user(username=username)
        ##user.is_admin = True
        ##user.save(using=self._db)
        ##return user
    
class User(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username',max_length=15, unique=True)
    password = models.CharField('Password',max_length=256)
    name = models.CharField('Name',max_length=30)
    email = models.EmailField('Email',max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects=UserManager()
    
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS=['email']
        