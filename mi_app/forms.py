from django import forms
from django.core import validators
from mi_app.models import Comments

class FormUser(forms.ModelForm):
    #Campos personalizados
    class Meta:
        model = Comments
        fields = '__all__'
        #exclurir campos
        #exclude = ['name']


#class FormUser(forms.Form):
#    name = forms.CharField(validators=[validators.MaxLengthValidator(5)])
#    email = forms.EmailField()
#    text = forms.CharField(widget=forms.Textarea)
#    atrapabots = forms.CharField(required=False, widget=forms.HiddenInput)

    #Funcion para verificar que los datos en atrapabots
#    def clean_atrapabots(self):
#        atrapador = self.cleaned_data['atrapabots']
#        if (len(atrapador) > 0):
#            raise forms.ValidationError('Te cache mi robocop!!!')
#        return atrapador
