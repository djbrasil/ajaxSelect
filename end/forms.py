from django import forms

from end.models import Solicitacao, Endereco


class solicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].queryset = Endereco.objects.none()

        if 'empresas' in self.data:
            try:
                empresas_id = int(self.data.get('empresas'))
                self.fields['text'].queryset = Endereco.objects.filter(empresas_id=empresas_id).order_by('name')
            except (ValueError, TypeError):
                pass 
 