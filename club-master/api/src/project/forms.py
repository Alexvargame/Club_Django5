from django import forms
from django.forms import fields, widgets
from src.models.enums import Status, Role

# from src.models.category import Category
# from src.models.stack import Stack
# from src.models.vacancy import Vacancy

class ProjectCreateForm(forms.Form):
    def __init__(self, *args, stacks=None, categories=None, **kwargs):
        super().__init__(*args, **kwargs)
        if stacks is not None:
            self.fields["stacks"] = forms.ModelMultipleChoiceField(
                queryset=stacks,
                required=True,
                # widget=forms.CheckboxSelectMultiple,
            )
        if categories is not None:
            self.fields["categories"] = forms.ModelMultipleChoiceField(
                queryset=categories,
                required=True,
                # widget=forms.CheckboxSelectMultiple,
            )


    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=5000, widget=forms.Textarea)
    repo_link = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices=Status)
    author_role = forms.ChoiceField(choices=Role)
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    # categories = forms.CharField(widget=forms.SelectMultiple(choices=[(cat.id, cat.name) for cat in Category.objects.all()],
    #                                                          attrs={'class':'form-control'}))

    # stacks = forms.CharField(widget=forms.SelectMultiple(choices=[(st.id, st.name) for st in Stack.objects.all()],
    #                                                                     attrs={'class':'form-control'}))
    stacks = forms.ModelMultipleChoiceField(queryset=None)
    categories = forms.ModelMultipleChoiceField(queryset=None)