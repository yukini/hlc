from django.db import models


class UserInfo(models.Model):
    kanji_name_first = models.CharField(max_length=20)
    kanji_name_last = models.CharField(max_length=20)
    kana_name_first = models.CharField(max_length=20)
    kana_name_last = models.CharField(max_length=20)

    post_code = models.CharField(max_length=20)
    kanji_address = models.CharField(max_length=100)
    kana_address = models.CharField(max_length=100)

    kanji_address_other = models.CharField(max_length=100)
    kana_address_other = models.CharField(max_length=100)

    tel = models.CharField(max_length=20)

    pub_date = models.DateTimeField('date published')
