from django.shortcuts import render,redirect
from django.views import View
from .models import Restaurant,Category,Review,Favorite,Reservation
from .forms import ReviewForm,FavoriteForm,ReservationForm
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

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



class RestaurantView(LoginRequiredMixin,View):
    def get(self,request,pk):
        
        print(pk)

        context = {}

        context["restaurant"] = Restaurant.objects.filter(id=pk).first()

        context["reviews"] = Review.objects.filter(restaurant=pk)

        return render(request, "restaurant.html",context)


class ReviewView(LoginRequiredMixin, View):
    def post(self,request,pk):

        print(pk, "に対してレビュー")

        restaurant = Restaurant.objects.filter(id=pk).first()
        request.user
        request.POST["content"]        

        """
        review = Review(restaurant=restaurant, user=request.user, content=request.POST["content"])
        review.save()   
        """
        
        copied = request.POST.copy()
        copied["user"] = request.user
        copied["restaurant"] = restaurant

        ReviewForm(copied)    

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print(form.errors)

        return redirect("top")


class FavoriteView(LoginRequiredMixin,View):
    def post(self, request,pk):
        restaurant = Restaurant.objects.filter(id=pk).first()

        copied = request.POST.copy()
        copied["user"] = request.user
        copied["restaurant"] = restaurant

        form = FavoriteForm(copied)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print(form.errors)

        return redirect("top")


class ReservationView(LoginRequiredMixin,View):
    def post(self, request,pk):

        restaurant = Restaurant.objects.filter(id=pk).first()   
        copied = request.POST.copy()
        copied["user"] = request.user
        copied["restaurant"] = restaurant


        form = ReservationForm(copied)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print(form.errors)

        return redirect("top")



class MypageView(LoginRequiredMixin,View):
    def get(self, request):

        context = {}

        context["favorites"] = Favorite.objects.filter(user=request.user)
        context["Reviews"] = Review.objects.filter(user=request.user)
        context["Reservations"] = Reservation.objects.filter(user=request.user)

        return render(request, "mypage.html", context)
