from django import forms
from django.contrib.auth.forms import UserCreationForm

from entry.models import EntryUser


class EntryUserForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)
    birth_date = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = EntryUser
        fields = (
            "email",
            "kanji_last_name",
            "kanji_first_name",
            "kana_last_name",
            "kana_first_name",
            "gender",
            "day_of_birth",
            "month_of_birth",
            "year_of_birth",
            "date_of_birth",
            "post_code",
            "kanji_address",
            "kanji_address_other",
            "kana_address",
            "kana_address_other",
            "tel",
            "tel_2"
        )
        widgets = {
            'kanji_address': forms.TextInput(attrs={'class': 'test'}),
            'gender': forms.RadioSelect()
        }
        initials = {
            'post_code': '2'
        }
        help_texts = {
            'email': 'help_text'
        }
