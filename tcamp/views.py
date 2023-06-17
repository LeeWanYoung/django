from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("장고 논산 훈련소에 오신걸 환영합니다.")

