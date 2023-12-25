from django.forms import ModelForm, TextInput
from tools.models import Dripper

class DripperForm(ModelForm):
    class Meta:
        model = Dripper
        fields = ('brand', 'model', )
        widgets = {
            "brand": TextInput(attrs={'class': 'form-control input input-bordered input-accent w-full max-w-xs'}),
            "model": TextInput(attrs={'class': 'form-control input input-bordered input-secondary w-full max-w-xs'}),
        }
