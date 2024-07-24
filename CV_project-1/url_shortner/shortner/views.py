from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
import random
import string

def generate_short_code():
    characters = string.digits + string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(5))

def home(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_code = generate_short_code()
        URL.objects.create(long_url=long_url, short_code=short_code)
        return render(request, 'shortner/home.html', {'short_url': request.build_absolute_uri('/') + short_code})
    return render(request, 'shortner/home.html')

def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    return redirect(url.long_url)