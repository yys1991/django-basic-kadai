from django.shortcuts import render
from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name="top.html"

from django.views import View
from.models import Restaurant,Category

from django.db.models import Q


class TopView(View):
    def get(self,request):
        query = Q()

        if"search" in request.GET:
           print(request.GET["search"])


           words = request.GET["search"].replace("　"," ").split(" ")
           print(words)


           for word in words:
               query &= Q(name__icontains=word)


        if "category" in request.GET:
            print( request.GET["category"] )       
            if "" != request.GET["category"]:
                query &= Q(category=request.GET["category"])


        restaurants = Restaurant.objects.filter(query)

        categories = Category.objects.all()

        context={
            "restaurants":restaurants,
            "greet":"こんにちは",
            "price":1000,
            "categories":categories
        }

        return render(request,"top.html",context)