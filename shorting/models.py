from django.db import models
from django.urls import reverse

from shorting.utils import short_url_generator
from shorting.utils import HOSTNAME

MAX = 15


class Link(models.Model):
    url = models.TextField(max_length=1000, unique=True)
    short_url = models.CharField(max_length=MAX, unique=True, db_index=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.short_url is None or self.short_url == '':
            i = 0
            while True:
                i += 1
                short_url = short_url_generator()
                qs = self.__class__.objects.filter(short_url=short_url, active=True)
                if not qs.exists() and short_url != 'static':
                    self.short_url = short_url
                    break
                if i > 100:
                    return 'TimeError. Number of tries exceeded a hundred'
        super().save(*args, **kwargs)

    def get_short_url(self):
        return HOSTNAME + reverse('shorting:redirect_view', args=(self.short_url,))

    def __str__(self):
        return f'Link( {self.url} | {self.short_url} )'