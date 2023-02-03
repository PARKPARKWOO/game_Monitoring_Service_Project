from django.db import models

# Create your models here.
class token(models.Model):
    token_num = models.TextField() # 토큰 수
    image = models.ImageField() # 원하는 사진
    ment = models.TextField()


