from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.

DEPARTMENT_CHOICES = (
    ("1", "HR"),
    ("2", "Finance"),

)

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, mobile_number, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not mobile_number:
            raise ValueError('The given mobile Number must be set')
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile_number, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile_number, password, **extra_fields)

    def create_superuser(self, mobile_number, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(mobile_number, password, **extra_fields)


class User(AbstractUser):
    mobile_number = models.IntegerField(unique=True)

    REQUIRED_FIELDS = ['mobile_number']


    objects = UserManager()

    def __str__(self):
        return str(self.mobile_number)


class Employee(models.Model):

    employee_code = models.CharField(max_length=255, unique=True)
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_code


