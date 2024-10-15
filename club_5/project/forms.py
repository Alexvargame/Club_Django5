from django import forms
from django.forms import fields, widgets
from .models import Status, Role, Category, Stack, Project


class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['author', 'name', 'description', 'repo_link', 'status', 'author_role',
                'deadline', 'categories', 'stacks']
        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'name': forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'description': forms.Textarea(attrs={'class':'form-control', 'empty_value':True}),
            'repo_link': forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'status': forms.Select(choices=Status),
            'author_role': forms.Select(choices=Role),
            'deadline': forms.DateTimeInput(attrs={'type': 'date'}),
            'categories': forms.SelectMultiple(choices=[(cat.id, cat.name) for cat in Category.objects.all()],
                                            attrs={'class': 'form-control'}),
            'stacks': forms.SelectMultiple(choices=[(st.id, st.name) for st in Stack.objects.all()],
                                                                 attrs={'class': 'form-control'})
        }

