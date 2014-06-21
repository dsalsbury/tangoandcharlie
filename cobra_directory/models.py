from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class MyUserManager(BaseUserManager):
    def create_user(self, username, firstname, lastname, year, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            firstname=firstname,
            lastname=lastname,
            year=year,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, firstname, lastname, year, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            year=year
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        blank=True,
    )

    username = models.CharField(max_length=200, blank=True, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    current_location = models.CharField(max_length=300, blank=True)
    current_job = models.CharField(max_length=300, blank=True)
    year = models.CharField(max_length=4)
    major = models.CharField(max_length=300, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'year']

    def get_firstname(self):
        return self.firstname

    def get_full_name(self):
        # The user is identified by their email address
        return self.firstname + " " + self.lastname

    def get_year(self):
        return self.year

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

