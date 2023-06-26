from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser = 인증기능에 있는 것
# Create your models here.
class User(AbstractUser):  # AbstractUser 로 상속받아서 전개함(관계형 DB)
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)
    registered_date = models.DateTimeField(auto_now_add=True)  # 현재시간

    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
