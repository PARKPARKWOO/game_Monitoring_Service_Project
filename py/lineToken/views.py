from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect, Http404
import requests
from .models import LineToken
from .form import line_update
from .urls import path


# Create your views here.
# 로그인후 홈으로
def home(request):
    template_name = "templates/lineToken/index.html"
    return render(request, template_name)

# 보낸 후 홈으로  ( 나중에 성공/실패 메시지 출력하는거로 바꾸기)
def send(request):
    template_name = "templates/lineToken/index.html"
    return render(request, template_name)

# 로그인 화면
def login(request):
    template_name = "templates/lineToken/login.html"
    return render(request, template_name)

# 보내는 값
def send_message(request):
    line = LineToken.objects.get(id="send_id")
    if request.method == "POST":
        form = line_update(request.POST)
        if form.is_valid():
            LineToken.want_message = request.POST["want_massage"]
            LineToken.line_token = request.POST["line_token"]
            LineToken.photo_input = request.POST["photo_input"]
            LineToken.save()
            return redirect("/lineToken/index.html")
    else:
        form = line_update(instance=line)
        return render(request, "lineToken/index.html", {"form":form})







