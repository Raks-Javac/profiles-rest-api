from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,password=None):
        """This functions create a new user profile object"""
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email = email,name = name)
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self,email,name,password):
        """This function creates a admin user with given details"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True2
        user.save(using = self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """This model represents the whole user profile in our system overwriting the custom model"""
    email = models.EmailField(max_length= 255,unique = True)
    name = models.CharField(max_length = 255)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    objects = UserProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_user_fullname(self):
        """This functions returns the user full name"""
        return self.name

    def get_short_name(self):
        """This functions returns the user first Name"""
        return self.name

    def __str__(self):
        """Django uses this method to convert an object to a string"""
        return self.email


class ProfileFeedItem(models.Model):
    """This model class is for profile status update ,synced to db"""

    user_profile = models.ForeignKey('UserProfile',on_delete = models.CASCADE)
    status_text = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        """This method returns our model object as a string"""
        return self.status_text
