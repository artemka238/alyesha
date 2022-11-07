from django.shortcuts import render, redirect
from .forms import Review_form
from .models import Review

# Create your views here.
def x(request):
    return render(request,"index.html")
def y(request):
    return render(request,"rar.html")
def z(request):
    return render(request,"rar2.html")
def review(request):
    if request.method == "POST":
        form = Review_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            name = data.get("name")
            mail = data.get("mail")
            rating = data.get("rating")
            review = data.get("review")
            Review.objects.create(name = name,rating = rating,mail = mail,review = review)
            return redirect("review")
    form = Review_form()
    review1 = Review.objects.all()
    return render(request,"main.html",{"key_f":form,"key_r":review1})