from django.shortcuts import render, redirect
from .forms import Review_form

# Create your views here.
def x(request):
    return render(request,"index.html")
def y(request):
    return render(request,"rar.html")
def z(request):
    return render(request,"rar2.html")
def review(request):
    if request.method == "GET":
        form = Review_form()
        return render(request,"main.html",{"key_f":form})
    elif request.method == "POST":
        form = Review_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return redirect("review")