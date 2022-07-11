from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy


class UrlStorage(models.Model):

    url_long = models.URLField(gettext_lazy('Url long'), max_length=2048)
    url_short = models.URLField(gettext_lazy('Url short'), max_length=256, unique=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_url',
        verbose_name=gettext_lazy('Owner'),
    )
    created = models.DateTimeField(gettext_lazy('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = gettext_lazy('UrlStorage')
        verbose_name_plural = gettext_lazy('Films genre')
        constraints = [
            models.UniqueConstraint(
                fields=('owner', 'url_long'),
                name='owner_url_long',
            ),
        ]
