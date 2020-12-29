from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    tmp = forms.BooleanField(),

    class Meta:
        model = Item
        fields = ('tmp', 'name', 'takuhaikenpin', 'sonotakenpin', 'nyuukosyouhinka', 'shiiresyouhinka',
                  'cleaning', 'dataerase', 'shiirePC', 'tsutaya', 'takuhaikaikon', 'picking', 'datanyuuryoku',
                  'created_at', 'memo')

        widgets = {
                    #'name': forms.TextInput(attrs={'placeholder':'記入例：山田　太郎'}),
                    'name': forms.Select(),
                    'takuhaikenpin': forms.NumberInput(attrs={'min': 0}),
                    'sonotakenpin': forms.NumberInput(attrs={'min': 0}),
                    'nyuukosyouhinka': forms.NumberInput(attrs={'min': 0}),
                    'shiiresyouhinka': forms.NumberInput(attrs={'min': 0}),
                    'cleaning': forms.NumberInput(attrs={'min': 0}),
                    'dataerase': forms.NumberInput(attrs={'min': 0}),
                    'shiirePC': forms.NumberInput(attrs={'min': 0}),
                    'tsutaya': forms.NumberInput(attrs={'min': 0}),
                    'takuhaikaikon': forms.NumberInput(attrs={'min': 0}),
                    'picking': forms.NumberInput(attrs={'min': 0}),
                    'datanyuuryoku': forms.NumberInput(attrs={'min': 0}),
                    'created_at': forms.DateTimeInput(),


                    #'sex': forms.RadioSelect(), ←ラジオボタン
                    # 'sex': forms.Select(),  # プルダウンセレクト
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }
