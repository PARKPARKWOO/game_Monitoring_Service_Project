from django.urls import path
from lineToken import views

# 작성후 python3 manage.py makemigrations lineToken 할것. 후에 python3 manage.py migrate
urlpatterns = [
    path("", views.send, name='lineToken'),
    path("send_message/<int:send_id>", views.send_message, name="send_massage"),
]
