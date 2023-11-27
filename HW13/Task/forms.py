from django import forms
from .models import *

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'descrption', 'start_date', 'end_date', 'start_time', 'end_time', 'user']
    # title = forms.CharField(max_length=100)
    # descrption = forms.CharField(max_length=500)
    # start_date = forms.DateField(default=jdatetime.datetime.today().strftime('%Y-%m-%d'))
    # start_time = forms.TimeField(default=timezone.now)
    # end_date = forms.DateField(default=jdatetime.datetime.today().strftime('%Y-%m-%d'))
    # end_time = forms.TimeField(default=timezone.now)
    # user = forms.ModelChoiceField(queryset=Users.objects.all())
    # completed = forms.BooleanField(default=False)
    # category = forms.ModelChoiceField(queryset=Categories.objects.all())