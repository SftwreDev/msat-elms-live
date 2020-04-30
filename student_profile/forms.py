from django import forms

from .models import StudentProfile
from bootstrap_modal_forms.forms import BSModalForm


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'



class ProfileForm(BSModalForm):
	class Meta:
		model = StudentProfile
		fields = '__all__'
