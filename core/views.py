from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'core/signup.html')

def signin(request):
    return render(request, 'core/signin.html')

def profile(request):
    return render(request, 'core/profile.html')