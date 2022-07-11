
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UrlToShortForm
from .models import UrlStorage
from .services import UrlShorter


@login_required
def save_short_url(request):
    if request.method == 'POST':
        long_url_form = UrlToShortForm(request.POST)
        if long_url_form.is_valid():
            long_url = long_url_form.cleaned_data['long_url']
            url_storage = UrlShorter(long_url=long_url, user=request.user).save_short_url()
            return render(request, 'short_url_success.html', {"url_storage": url_storage})
    long_url_form = UrlToShortForm()
    return render(request, 'url_form.html', {"form": long_url_form})


def main_page(request):
    urls = None
    if request.user.is_authenticated:
        urls = UrlStorage.objects.filter(owner=request.user)
    return render(request, "main_page.html", {'urls': urls})
