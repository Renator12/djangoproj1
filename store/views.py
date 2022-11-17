from django.shortcuts import render
from .models import Project
# Create your views here.
def store(request):
    project=Project.objects.all()
    return render(request,'store/store1.html',{'projects':project})
def cart(request):
    return render(request,'store/cart.html')
def checkout(request):
    return render(request,'store/CHECKOUT.html')