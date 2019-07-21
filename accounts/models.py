from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings




# Create your models here.
class User(AbstractUser):
    
    username = models.CharField(max_length = 25,blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone_regex = RegexValidator(regex= r'^\+?1?\d{9,14}$', message = "Phone Number Format should be of Format +99999999")
    phone_number = models.CharField(validators = [phone_regex], max_length = 15, null=True)

