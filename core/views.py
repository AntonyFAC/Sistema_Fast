from django.shortcuts import render
from core import *
# Create your views here.
def home(request):
    return render(request, "core/home.html")
def visit(request):
    return render(request, "core/visit.html")
def blog(request):
    return render(request, "core/blog.html")
def contact(request):
    return render(request, "core/contact.html")
def history(request):
    return render(request, "core/history.html")
def other(request):
    return render(request, "core/other.html")