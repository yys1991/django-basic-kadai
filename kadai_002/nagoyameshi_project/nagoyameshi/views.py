from django.shortcuts import render
from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name="top.html"

from django.views import View
from.models import Restaurant

class TopView(View):
    def get(self,request):
        if"search" in request.GET:
            print(request.get["search"])

        restaurants=Restaurant.objects.all()

        context={"restaurants":restaurants,
                 "greet":"こんにちは",
                 "price":1000
        }         
        return render(request,"top.html",context)