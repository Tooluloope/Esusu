from django.db import models

# Create your models here.
class Groups(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    no_of_members = models.IntegerField()
    savings = models.IntegerField()
    description = models.TextField()
    begin_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    searchable = models.BooleanField(default = False)
    members = models.ManyToManyField(User)
    created_by = models.ForeignKey(User)
    

    
