import django.forms as forms


class LicenseCreationForm(forms.Form):
    qty = forms.IntegerField(label='qty')
    dur = forms.IntegerField(label='duration')

    def __str__(self):
        print(self.dur)

class Snippet(forms.Form):
    body = forms.CharField(label='input licences',
                           widget=forms.Textarea())
