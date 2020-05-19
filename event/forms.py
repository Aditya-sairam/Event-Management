from django import forms 
from .models import Event

class EventRegisterForm(forms.ModelForm):
	class Meta:
		model = Event 
		fields = ['full_name','mobile_number','id_card','registration_type','number_of_tickets']


class PostSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    
                    widget=forms.TextInput(attrs={'placeholder': 'search by name!'})
                  )

    search_reg_exact = forms.IntegerField(
                    required = False,
                    
                  )
