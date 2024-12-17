from django import forms

from django.contrib.auth.models import User

from todolist_dtos.models.cost import Cost
from todolist_dtos.models.category_cost import CategoryCost

class CategoryCostForm(forms.ModelForm):

    class Meta:
        model = CategoryCost
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'empty_value':True})
        }

class CostCreateForm(forms.ModelForm):

    class Meta:
        model = Cost
        fields = ('user', 'category', 'cost_date', 'cost_name', 'cost_sum')
        widgets ={
            'user':forms.Select(choices=[(us.id, us.username) for us in User.objects.all()],
                                                   attrs={'class': 'form-control', 'empty_value': True}),
            'category': forms.Select(choices=[(cat.id, cat.name) for cat in CategoryCost.objects.all()],
                                       attrs={'class': 'form-control', 'empty_value': True}),
            'cost_date':forms.DateInput(attrs={'class': 'form-control', 'empty_value': True, 'type': 'date'}),
            'cost_name': forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'cost_sum': forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
        }

class CostManyCreateForm(forms.Form):

    user = forms.CharField(label='Пользователь',
                             widget=forms.Select(choices=[(us.id,us.username) for us in User.objects.all()],attrs={'class':'form-control', 'empty_value':True}))
    category = forms.CharField(label='Категория',
                             widget=forms.Select(choices=[(cat.id,cat.name) for cat in CategoryCost.objects.all()],attrs={'class':'form-control', 'empty_value':True}))
    cost_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'empty_value': True,'type': 'date'}))

class CostForm(forms.Form):

    cost_name = forms.CharField(label='Назначение',required=False, widget=forms.TextInput(attrs={'class':'form-control', 'empty_value':True}))
    cost_sum = forms.DecimalField(label='Сумма', initial=0.00, widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
