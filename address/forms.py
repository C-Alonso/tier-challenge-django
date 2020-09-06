from django import forms
# from .validators import validate_url
from .models import Address
from .validators import validate_url

class AddressCreateForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}),validators=[validate_url]) #required is True by default.
    
    class Meta:
        model = Address
        fields = ['address']

    