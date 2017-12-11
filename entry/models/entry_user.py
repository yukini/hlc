from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# https://docs.djangoproject.com/ja/2.0/topics/auth/customizing/#a-full-example
class EntryUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a email address')
        email = EntryUserManager.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class EntryUser(AbstractBaseUser):
    email = models.EmailField(max_length=128, unique=True)

    kanji_first_name = models.CharField(max_length=20)
    kanji_last_name = models.CharField(max_length=20)
    kana_first_name = models.CharField(max_length=20)
    kana_last_name = models.CharField(max_length=20)

    # https://docs.djangoproject.com/en/dev/ref/models/instances/#extra-instance-methods
    GENDER_DIVISION = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    # djangoのModelFormはどこでchoicesに「-------」を入れているのか追いかけてみた
    # http://y0m0r.hateblo.jp/entry/20130421/1366533452
    gender = models.CharField(
        max_length=1, choices=GENDER_DIVISION, default='M')

    day_of_birth = models.CharField(max_length=2)
    month_of_birth = models.CharField(max_length=2)
    year_of_birth = models.CharField(max_length=4)
    date_of_birth = models.DateField(null=True)

    post_code = models.CharField(max_length=20)
    kanji_address = models.CharField(max_length=100)
    kana_address = models.CharField(max_length=100)
    kanji_address_other = models.CharField(max_length=100)
    kana_address_other = models.CharField(max_length=100)

    tel = models.CharField(max_length=20)
    tel_2 = models.CharField(max_length=20, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    # マネージドアトリビュー ト (managed attribute)
    # http://qh73xebitbucketorg.readthedocs.io/ja/latest/1.Programmings/python/LIB/django/model/main/#id4
    def _get_full_kanji_name(self) -> str:
        "Returns the person's full name."
        return '%s %s' % (self.kanji_last_name, self.kanji_first_name)
    full_kanji_name = property(_get_full_kanji_name)

    def _get_full_kana_name(self) -> str:
        "Returns the person's full name."
        return '%s %s' % (self.kana_last_name, self.kana_first_name)
    full_kana_name = property(_get_full_kana_name)

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('entry:confirm', kwargs={})

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = EntryUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_staff

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_staff

    @property
    def is_staff(self):
        return self.is_admin
