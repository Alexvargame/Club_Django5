from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from real_estate.forms import FlatCreateForm, HouseCreateForm
from real_estate.dtos.request.create_real_estate_dto import CreateFlatDTO, CreateHouseDTO
from real_estate.repository import FlatRepository, HouseRepository
from real_estate.controllers.utils import ObjectCreateMixin


class FlatCreateView(LoginRequiredMixin, ObjectCreateMixin, View):
    form = FlatCreateForm
    template = 'real_estate/create_flat.html'
    redirect_success = 'list_real_estates'
    redirect_lose = 'create_flat'
    model_dto = CreateFlatDTO
    rep = FlatRepository

    # def get(self,request):
    #     form = FlatCreateForm(initial={'floor':1 , 'number_of_storeys': 1, 'square': 1,
    #                                    'price': 1, 'number_address_building': 1, 'number_address_appart': 1,
    #                                    })
    #     return render(request, 'real_estate/create_flat.html', {'form':form})
    #
    # def post (self, request):
    #     form = FlatCreateForm(request.POST)
    #     # form.cleaned_data.pop('city') - Пример
    #     if form.is_valid():
    #         data = CreateFlatDTO(
    #             **form.cleaned_data,
    #             author = request.user,
    #             site_link = 'www.site.'+str(form.cleaned_data['id_object'])
    #         )
    #         RealEstateService(FlatRepository()).create_object(data)
    #         return redirect('list_real_estates')
    #     return redirect('create_flat')

class HouseCreateView(LoginRequiredMixin, ObjectCreateMixin, View):
    form = HouseCreateForm
    template = 'real_estate/create_house.html'
    redirect_success = 'list_real_estates'
    redirect_lose = 'create_house'
    model_dto = CreateHouseDTO
    rep = HouseRepository
