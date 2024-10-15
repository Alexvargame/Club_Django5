from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from estate.models.flat import Flat
from estate.models.house import House
from real_estate.forms import FlatCreateForm, HouseCreateForm
from real_estate.dtos.response.detail_real_estate_dto import FlatDTO, HouseDTO
from real_estate.repository import FlatRepository, HouseRepository
from real_estate.controllers.utils import ObjectUpdateMixin

# from django.shortcuts import render, redirect
# from real_estate.real_estate_service import RealEstateService


class FlatUpdateView(LoginRequiredMixin, ObjectUpdateMixin, View):
    form = FlatCreateForm
    model = Flat
    template = 'real_estate/update_flat.html'
    redirect_success = 'list_user_real_estates'
    redirect_lose = 'update_flat'
    model_dto = FlatDTO
    rep = FlatRepository


    # def get(self,request, pk):
    #     flat = Flat.objects.get(id=pk)
    #     form = FlatCreateForm(initial=RealEstateService(FlatRepository()).detail_object(flat).__dict__)
    #     return render(request, 'real_estate/update_flat.html', {'form':form})
    #
    # def post (self, request,pk):
    #     flat = Flat.objects.get(id=pk)
    #     form = FlatCreateForm(request.POST, initial=RealEstateService(FlatRepository()).detail_object(flat).__dict__)
    #     # form.cleaned_data.pop('city') - Пример
    #     if form.is_valid():
    #         data = CreateFlatDTO(
    #             **form.cleaned_data,
    #             author = request.user,
    #             site_link = 'www.site.'+str(form.cleaned_data['id_object'])
    #         )
    #         RealEstateService(FlatRepository()).create_object(data)
    #         return redirect('list_real_estates')
    #     return redirect('update_flat')

class HouseUpdateView(LoginRequiredMixin, ObjectUpdateMixin, View):
    form = HouseCreateForm
    model = House
    template = 'real_estate/update_house.html'
    redirect_success = 'list_user_real_estates'
    redirect_lose = 'update_house'
    model_dto = HouseDTO
    rep = HouseRepository
