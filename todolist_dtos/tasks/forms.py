from django import forms

from todolist_dtos.models.category import CategoryTask
from todolist_dtos.models.task import Task
from todolist_dtos.models.priority import Priority
from todolist_dtos.models.dayplan import DayPlan

class TaskForm(forms.ModelForm):
    #category_cost = forms.CharField(
    #     widget=forms.Select(choices=sorted([(obj.name, obj.name) for obj in CategoryTask.objects.all()]),
    #                         attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['name', 'priority', 'date_create', 'date_to_do', 'description', 'status', 'remark', 'category']
        widgets = {
            # 'user':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'empty_value': True}),
            'priority': forms.Select(choices=sorted([(obj.priority, obj.priority) for obj in Priority.objects.all()]),
                                     attrs={'class': 'form-control'}),
            'category': forms.Select(choices=sorted([(obj.name, obj.name) for obj in CategoryTask.objects.all()]),
                            attrs={'class': 'form-control'}),

            # 'category':forms.Select(choices=sorted([(obj.name,obj.name) for obj in CategoryTask.objects.all()]),attrs={'class':'form-control'}),
            'date_create': forms.DateInput(attrs={'class': 'form-control', 'empty_value': True, 'type': 'date'}),
            'date_to_do': forms.DateInput(attrs={'class': 'form-control', 'empty_value': True, 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'empty_value': True}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'empty_value': True}),
            'status': forms.Select(choices=[(True, True), (False, False)], attrs={'class': 'form-control'}),

        }

class CreateDayForm(forms.ModelForm):
    class Meta:
        model=DayPlan
        fields=['day_date']
        widgets={
            'day_date':forms.DateInput(attrs={'class':'form-control', 'empty_value':True,'type':'date'}),
           }


class CreateDayTasksForm(forms.Form):

    tasks = forms.CharField(label='Задания на выбор', required=False,
                          widget=forms.CheckboxSelectMultiple(choices=[(t.name,t.name) for t in Task.objects.all()],
                          attrs={'class':'form-control'}))

class ChoiceDayForm(forms.Form):

    choice_day = forms.DateField(label='Выберите дату',widget=forms.DateInput(attrs={'class':'form-control', 'empty_value':True,'type':'date'}))
