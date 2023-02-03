from django.shortcuts import render
from rest_framework.views import APIView


class main(APIView):
    def get(self, request):
        print("겟으로 호출")
        return render(request, "GMS/use_GMS.html")

    def post(self, request):
        print("포스트로 호출")
        return render(request, "GMS/index.html")