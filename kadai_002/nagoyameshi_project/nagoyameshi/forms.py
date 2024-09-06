from django import forms
from . models import Review,Favorite



class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [ "restaurant","user","content" ]



class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ["restaurant","user"]