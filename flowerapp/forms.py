from django import forms
from .models import flower
class flowerform(forms.ModelForm):
     class Meta:
         model=flower
         fields=['name','sname','desc','img']

