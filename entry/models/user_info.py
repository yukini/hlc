from django.db import models
from django.utils import timezone


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

    def post(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pub_date

    # マネージドアトリビュー ト (managed attribute)
    # http://qh73xebitbucketorg.readthedocs.io/ja/latest/1.Programmings/python/LIB/django/model/main/#id4
    def _get_full_kanji_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.kanji_name_last, self.kanji_name_first)
    full_kanji_name = property(_get_full_kanji_name)

    def _get_full_kana_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.kana_name_last, self.kana_name_first)
    full_kana_name = property(_get_full_kana_name)
