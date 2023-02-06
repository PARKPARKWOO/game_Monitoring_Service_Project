from django.urls import path
from home import views
# 홈페이지 값 입력받으면
urlpatterns = [
    path("", views.index, name="index"),
]
