from django import forms
from django.utils import timezone

from entry.models import UserInfo


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = (
            "kanji_name_last",
            "kanji_name_first",)
