from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, name, username, email, gender, password=None):
        if not email:
            raise ValueError('이메일을 확인해주세요')

        if not username:
            raise ValueError('닉네임을 지정해주세요')

        user = self.model(
            # normalize changes capital to small case
            email=self.normalize_email(email),
            username=username,
            name=name,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, name, email, username, password, gender):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username + '_GM',
            password = password,
            name = name,
            gender = gender,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, '남자'), (GENDER_FEMALE, '여자')]
    gender = models.IntegerField(choices=GENDER_CHOICES)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'gender']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
