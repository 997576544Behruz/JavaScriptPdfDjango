from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices
from django_quill.fields import QuillField

# Create your models here.


class Employee(models.Model):
    ismi=models.CharField(max_length=100)
    familya=models.CharField(max_length=100)
    otasining_ismi=models.CharField(max_length=100)
    ishga_kirgan_vaqti=models.DateField()
    tugilgan_yili=models.DateField()
    content = QuillField()

    status_millat = Choices('Uzbek', 'Qozoq','Rus','Tojik')
    millati=StatusField(choices_name = 'status_millat')

    malumoti=models.CharField(max_length=100)
    mutaxasisligi=models.CharField(max_length=300)
    chet_tili=models.CharField(max_length=100)

    STATUS_m = Choices('ha',"yo'q")
    davlat_mukofati=StatusField(choices_name = 'STATUS_m')
    STATUS_d = Choices('ha',"yo'q")
    deputatmi=StatusField(choices_name = 'STATUS_d')
    t_joyi=models.CharField(max_length=100)
    partiyaviyligi=models.CharField(max_length=100)
    tamomlagan_joyi=models.CharField(max_length=100)
    ilmiy_unvoni=models.CharField(max_length=100)
    harbiy_unvoni=models.CharField(max_length=100)
    img=models.ImageField(upload_to='user/')

    def __str__(self):
        return self.ismi