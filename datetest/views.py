from datetime import datetime
from random import random

from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

class DataView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)

class RandomView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        rand_number = random()

        return HttpResponse(rand_number)