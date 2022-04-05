from .models import Mcomment
from django import forms
import datetime
from django.forms import SelectDateWidget


class commentForm(forms.Form):
    name = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            "placeholder": "익명"
        })
    )
    content = forms.CharField(max_length=350,
        widget=forms.Textarea(
            attrs={
                "placeholder": "타인의 권리를 침해하거나 명예를 훼손하는 댓글은 운영원칙 및 관련 법률에 제제를 받을 수 있습니다 ",
                'cols': 100, 'rows': 5
            })
    )