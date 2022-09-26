from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def search(request):
    return render(request,'blog/search.html')
