from django.forms import Form, ModelChoiceField, CharField
from grinder.models import GrinderBrand


class GrinderForm(Form):
    model = CharField()
    brand = ModelChoiceField(queryset=GrinderBrand.objects.all().order_by("id"), empty_label="-------------", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
        self.fields['brand'].widget.attrs['class'] = 'select select-bordered w-full max-w-xs'

        self.fields['model'].widget.attrs['class'] = 'form-control input input-bordered w-full max-w-xs'
        self.fields['model'].widget.attrs['placeholder'] = 'Put name here'
