from django import forms
from ad_app.models import  Adventure
from  ad_app.models import  Guide


class adventurepageform(forms.ModelForm):
    class Meta:
        model= Adventure
        fields= "__all__"

class guide_form(forms.ModelForm):
    class Meta:
        model = Guide
        fields = "__all__"