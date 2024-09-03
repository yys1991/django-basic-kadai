from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

class IndexView(View):

    def get(self, request, *args, **kwargs):

        return render(request,"nagoyameshi/index.html")

index   = IndexView.as_view()

class TopView(TemplateView):
    template_name="top.html"

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






class RestaurantView(View):
    def get(self,request,pk):
        
        print(pk)

        context = {}

        context["restaurant"] = Restaurant.objects.filter(id=pk).first()

        return render(request, "restaurant.html",context)


class ReviewView(View):
    def post(self,request):        

        return redirect("top")


from django.shortcuts import render,redirect

from django.views import View
from .models import Topic

class IndexView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        posted  = Topic( comment = request.POST["comment"] )
        posted.save()

        return redirect("bbs:index")

index   = IndexView.as_view()
