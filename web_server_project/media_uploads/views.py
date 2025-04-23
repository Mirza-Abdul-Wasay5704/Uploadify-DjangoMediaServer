# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    # Public landing page
    return render(request, 'media_uploads/home.html')

@login_required
def dashboard(request):
    # User dashboard showing their uploads
    return render(request, 'media_uploads/dashboard.html')