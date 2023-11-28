from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    verified = models.BooleanField(default=True)
    pricing_plan = models.CharField(max_length=100, default='Free', null=True, blank=True)
    email = models.CharField(max_length=1000,  null=True, blank=True)
    user_name = models.CharField(max_length=1000, null=True, blank=True)
    comments = models.IntegerField(default=0, null=True, blank=True)
    reviews = models.IntegerField(default=0, null=True, blank=True)
    number_of_created_watch_parties = models.IntegerField(default=0)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
def get_user_profile(self):

    return Profile.objects.get(user=self)

User.add_to_class("get_user_profile",get_user_profile)
