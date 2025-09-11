from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    otp = models.CharField(unique=True, max_length=6, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        email_username, full_name = self.email.split('@')
        if self.full_name == '' or self.full_name is None:
            self.full_name = email_username
        if self.username == '' or self.username is None:
            self.username = email_username
        super(CustomUser, self).save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='user_pics/', default="default-user.jpg", blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.full_name:
            return str(self.full_name)
        return str(self.user.full_name)
    
    def save(self, *args, **kwargs):
        if self.full_name == '' or self.full_name is None:
            self.full_name = self.user.full_name
        super(UserProfile, self).save(*args, **kwargs)
        
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)   
        
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
post_save.connect(create_user_profile, sender=CustomUser)
post_save.connect(save_user_profile, sender=CustomUser)
