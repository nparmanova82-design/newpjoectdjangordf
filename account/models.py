from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.text import slugify

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Phont_number bo'lishi shart")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_fields)

class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True,blank=False,null=False)
    phone_number=models.CharField(blank=False,null=False,max_length=15)
    age=models.PositiveIntegerField(default=18)
    bio=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True,unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['phone_number','age']
    objects=CustomUserManager()

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(f"{self.first_name}-{self.last_name}")
        super().save(*args,**kwargs)

    def str(self):
        return self.username