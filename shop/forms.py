from django.forms import ModelForm

from shop.models import Support


class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = [
            'name',
            'email',
            'message'
        ]
