from django.contrib.auth.models import AbstractUser
from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Vous devez renter un email.")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields

        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    firstname = models.CharField(max_length=50, verbose_name="Nom")
    lastname = models.CharField(max_length=50, verbose_name="Prénom")
    email = models.EmailField(unique=True, max_length=255, blank=True, verbose_name="Email")
    phone_number = models.CharField(max_length=13, unique=True, null=False, blank=False, verbose_name="Numéro de téléphone")
    password = models.CharField(max_length=15, blank=False, verbose_name="Mot de passe")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["firstname", "lastname", "email"]
    object = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
