from django.db import models
from django.contrib.auth.models import AbstractBaseUser
#from django.contrib.auth.models import PermissionMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password = None):
        """ Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Create and save a new superuser with given"""

        user = self.create_user(email, name, password)

        user.is_superuser = AbstractBaseUser
        user.is_staff = AbstractBaseUser
        user.save(using = self._db)

        return user


class UserProfile(AbstractBaseUser):
    """"Database model for users in the system"""

    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_fulle_name(self):
        """Retrieve full name of user"""
        return self.NAME

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.NAME

    def __str__(self):
        """return string representation of user"""
        return self.email
