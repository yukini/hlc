from django.db import models
from django.utils import timezone


class CompanyInfo(models.Model):
    uuid = models.UUIDField(primary_key=False, editable=False)

    name = models.CharField(max_length=200)

    post_code = models.CharField(max_length=20)
    kanji_address = models.CharField(max_length=100)
    kana_address = models.CharField(max_length=100)

    kanji_address_other = models.CharField(max_length=100)
    kana_address_other = models.CharField(max_length=100)

    tel = models.CharField(max_length=20)
    tel_2 = models.CharField(max_length=20)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('entry:confirm', kwargs={})
