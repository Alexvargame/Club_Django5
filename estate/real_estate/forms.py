from django import forms
from django.forms import widgets, fields

from estate.models.enums import TypeFlat, TypeHouse
from estate.models.comments import Comment

class FlatCreateForm(forms.Form):
    def __init__(self, *args, city=None, district=None, street=None, **kwargs):
        super().__init__(*args, **kwargs)
        if city is not None:
            self.fields['city'] = forms.ModelChoiceField(
                queryset=city,
                required=True,
                widget=forms.Select(attrs={'class': 'form-control', 'empty_value': True})

                # widget=forms.CheckboxSelectMultiple,
            )
        if district is not None:
            self.fields["district"] = forms.ModelChoiceField(
                queryset=district,
                required=True,
                widget=forms.Select(attrs={'class': 'form-control', 'empty_value': True})

                # widget=forms.CheckboxSelectMultiple,
            )
        if street is not None:
            self.fields["street"] = forms.ModelChoiceField(
                queryset=street,
                required=True,
                widget=forms.Select(attrs={'class': 'form-control', 'empty_value': True})

                # widget=forms.CheckboxSelectMultiple,
            )

    #id_object = forms.CharField(max_length=20)
    type = forms.ChoiceField(choices=TypeFlat, widget=forms.Select(attrs={'class':'form-control', 'empty_value':True}))
    floor = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    number_of_storeys = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    square = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    city = forms.ModelChoiceField(queryset=None)
    district = forms.ModelChoiceField(queryset=None)
    street = forms.ModelChoiceField(queryset=None)
    number_address_building = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', 'empty_value': True}))
    number_address_appart = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', 'empty_value': True}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    description = forms.CharField(max_length=5000, required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'empty_value': True}))
    rooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))

class FlatDeleteForm(forms.Form):
    pass
class HouseCreateForm(forms.Form):
    def __init__(self, *args, city=None, district=None, street=None, **kwargs):
        super().__init__(*args, **kwargs)
        if city is not None:
            self.fields['city'] = forms.ModelChoiceField(
                queryset=city,
                required=True,
                widget=forms.Select(attrs={'class': 'form-control', 'empty_value': True})
                # widget=forms.CheckboxSelectMultiple,
            )
        if district is not None:
            self.fields["district"] = forms.ModelChoiceField(
                queryset=district,
                required=True,
                widget=forms.Select(attrs={'class': 'form-control', 'empty_value': True})
                # widget=forms.CheckboxSelectMultiple,
            )
        if street is not None:
            self.fields["street"] = forms.ModelChoiceField(
                queryset=street,
                required=True,
                widget=forms.Select(attrs={'class':'form-control', 'empty_value':True})
                #forms.CheckboxSelectMultiple,
            )
    #id_object = forms.CharField(max_length=20)
    type = forms.ChoiceField(choices=TypeHouse, widget=forms.Select(attrs={'class':'form-control', 'empty_value':True}))
    area = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    square = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    city = forms.ModelChoiceField(queryset=None)
    district = forms.ModelChoiceField(queryset=None)
    street = forms.ModelChoiceField(queryset=None)
    number_address_building = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control', 'empty_value':True}))
    number_address_appart = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control', 'empty_value':True}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    description =forms.CharField(max_length=5000, required=False, widget=forms.Textarea(attrs={'class':'form-control', 'empty_value':True}))
    rooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))

class FlatSearchForm(forms.Form):
    def __init__(self, *args, cities=None, districts=None, streets=None, **kwargs):
        super().__init__(*args, **kwargs)
        if cities is not None:
            self.fields['cities'] = forms.ModelMultipleChoiceField(
                queryset=cities,
                required=True,
                widget=forms.SelectMultiple(attrs={'class': 'form-control', 'empty_value': True}),
                #widget=forms.CheckboxSelectMultiple,
            )
        if districts is not None:
            self.fields["districts"] = forms.ModelMultipleChoiceField(
                queryset=districts,
                required=True,
                widget=forms.SelectMultiple(attrs={'class': 'form-control', 'empty_value': True})
                # widget=forms.CheckboxSelectMultiple,
            )
        if streets is not None:
            self.fields["streets"] = forms.ModelMultipleChoiceField(
                queryset=streets,
                required=True,
                widget=forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True})
                #forms.CheckboxSelectMultiple,
            )
    type = forms.MultipleChoiceField(choices=TypeFlat, widget=forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True}))
    floor_at = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    floor_to = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    number_of_storeys_at = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    number_of_storeys_to= forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    cities = forms.ModelMultipleChoiceField(queryset=None)
    districts = forms.ModelMultipleChoiceField(queryset=None)
    streets = forms.ModelMultipleChoiceField(queryset=None)
    price_at= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    square_at = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    price_to = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    square_to = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    rooms_at = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    rooms_to = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))

class HouseSearchForm(forms.Form):
    def __init__(self, *args, cities=None, districts=None, streets=None, **kwargs):
        super().__init__(*args, **kwargs)
        if cities is not None:
            self.fields['cities'] = forms.ModelMultipleChoiceField(
                queryset=cities,
                required=True,
                widget=forms.SelectMultiple(attrs={'class': 'form-control', 'empty_value': True}),
                #widget=forms.CheckboxSelectMultiple,
            )
        if districts is not None:
            self.fields["districts"] = forms.ModelMultipleChoiceField(
                queryset=districts,
                required=True,
                widget=forms.SelectMultiple(attrs={'class': 'form-control', 'empty_value': True})
                # widget=forms.CheckboxSelectMultiple,
            )
        if streets is not None:
            self.fields["streets"] = forms.ModelMultipleChoiceField(
                queryset=streets,
                required=True,
                widget=forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True})
                #forms.CheckboxSelectMultiple,
            )
    type = forms.MultipleChoiceField(choices=TypeHouse, widget=forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True}))
    area_at = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    area_to = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    cities = forms.ModelMultipleChoiceField(queryset=None)
    districts = forms.ModelMultipleChoiceField(queryset=None)
    streets = forms.ModelMultipleChoiceField(queryset=None)
    price_at= forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}))
    square_at = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    price_to = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    square_to = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    rooms_at = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))
    rooms_to = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'empty_value': True}))

class ChoiceDateForm(forms.Form):
    date_at = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'empty_value':True, 'type':'date'}))
    date_to = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'empty_value': True, 'type': 'date'}))
    type_flat = forms.MultipleChoiceField(choices=TypeFlat, required=False,
                                     widget=forms.SelectMultiple(attrs={'class': 'form-control', 'empty_value': True}),)
    type_house = forms.MultipleChoiceField(choices=TypeHouse, required=False,
                                           widget=forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True}))


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('is_active', )
        widgets = {'real_state': forms.HiddenInput}

class GuestCommetForm(forms.ModelForm):
    #captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid': 'Неправильный текст'})

    class Meta:
        model = Comment
        exclude = ('is_active', )
        widgets = {'real_state': forms.HiddenInput}
