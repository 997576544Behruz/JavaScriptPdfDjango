from pyexpat import model
from django import forms
from .models import Employee
from django.contrib.auth.forms import UserChangeForm
class AddHomeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=[
    'ismi',
    'familya',
    'otasining_ismi',
    'ishga_kirgan_vaqti',
    'tugilgan_yili',
    'millati',
    'malumoti',
    'mutaxasisligi',
    'chet_tili',
    'davlat_mukofati',
    'deputatmi',
    't_joyi',
    'partiyaviyligi',
    'tamomlagan_joyi',
    'ilmiy_unvoni',
    'harbiy_unvoni',
    'content',
    'img'
    ]
class UpdateBlogForm(UserChangeForm):
    class Meta:
        model=Employee
        fields=[
            'ismi',
    'familya',
    'otasining_ismi',
    'ishga_kirgan_vaqti',
    'tugilgan_yili',
    'millati',
    'malumoti',
    'mutaxasisligi',
    'chet_tili',
    'davlat_mukofati',
    'deputatmi',
    't_joyi',
    'partiyaviyligi',
    'tamomlagan_joyi',
    'ilmiy_unvoni',
    'harbiy_unvoni',
    'content',
    'img'
        ]