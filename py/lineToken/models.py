from django.db import models
# Create your models here.

# 입력 받는 값
class LineToken(models.Model):
    line_token = models.CharField(max_length=200, unique=True) # 토큰 번호 입력 받기
    photo_input = models.ImageField() # 사진 입력 받기
    want_message = models.CharField(max_length=200)  # 원하는 멘트 받기

    def __str__(self):
        return self.line_token


#class message(models.Model):
#    tOKEN_Num = models.CharField(max_length=100) # 토큰 번호
#    image = models.ImageField() # 원하는 메시지
#    want_message = models.CharField(max_length=100) # 원하는 메시지 출력



