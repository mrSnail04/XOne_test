from django import forms
from django.utils.translation import gettext_lazy


class UrlToShortForm(forms.Form):
    long_url = forms.URLField(label=gettext_lazy('Long url'), required=True, widget=forms.Textarea)
