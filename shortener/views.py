import string
from django.shortcuts import get_object_or_404, render, redirect
import string
import random

from shortener.models import URLs


# Create your views here.
def home(request):
    return render(request, 'shortener/index.html')

def short(request):
    #breakpoint()
    #pass
    url = request.POST['url']

    try:
        while True:
            #Keep generating new url until it is unique
            shortURL = short_url()
            #Keep trying until exception is thrown
            URLs.objects.get(shortURL=shortURL)
    except URLs.DoesNotExist:
        #Now we are sure url is unique, save it!
        URLs(shortURL=shortURL, longURL=url).save()
    return render(request, 'shortener/index.html', context={'shortURL': shortURL})
def redirect_short_url(request, shortURL):
    url = get_object_or_404(URLs, shortURL=shortURL)
    return redirect(url.longURL)


def short_url():
    url = ''
    string_digits = string.ascii_letters + string.digits

    for i in range(7):
        url += random.choice(string_digits)

        return url
