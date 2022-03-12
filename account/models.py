from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from account.managers import UserManager


class DateAbstractModel(models.Model):
    date_created = models.DateTimeField(default=timezone.now())
    date_updated = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True


class PersonalArea(models.Model):
    PAYMENT_STATUS = (
        ('free', 'free'),
        ('payment', 'payment')
    )
    user = models.OneToOneField('UserModel', on_delete=models.CASCADE, related_name='personal_area', blank=True,
                                null=True)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS, default=PAYMENT_STATUS[0])
    check = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    logo = models.ImageField(upload_to='logos/')


class UserModel(AbstractBaseUser, DateAbstractModel, PermissionsMixin):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        super(UserModel, self).save(*args, **kwargs)
        personal = PersonalArea.objects.get(id=self.id)
        if not personal:
            PersonalArea.objects.create(user_id=self.id)
