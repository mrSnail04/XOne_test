from django.urls import path

from .views import main_page, save_short_url

app_name = "url_shorter"

urlpatterns = [
    path("url_form/", save_short_url, name='url_form'),
    path("", main_page, name='main_page')
]