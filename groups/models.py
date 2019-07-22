from django.db import models
from accounts.models import User, UserProfile
import uuid
from django.conf import settings


# Create your models here.
class Groups(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    group_id = models.UUIDField(default = uuid.uuid4, editable = False)
    no_of_members = models.PositiveIntegerField()
    savings_amount = models.PositiveIntegerField()
    
    description = models.TextField(blank=True, null=True)
    begin_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    searchable = models.BooleanField(default = True)
    members = models.ManyToManyField(User, related_name='group_members')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete =models.CASCADE,related_name='group_admin', null=True )

    def __str__(self):
        return self.name
    