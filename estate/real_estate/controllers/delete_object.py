from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from estate.models.flat import Flat
from estate.models.house import House

from real_estate.dtos.response.detail_real_estate_dto import FlatDTO, HouseDTO
from real_estate.repository import FlatRepository, HouseRepository
from real_estate.controllers.utils import ObjectDeleteMixin

class FlatDeleteView(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Flat
    template = 'real_estate/delete_flat.html'
    redirect_success = 'list_user_real_estates'
    model_dto = FlatDTO
    rep = FlatRepository

    # def get(self,request, pk):
    #     flat = Flat.objects.get(id=pk)
    #     dto = RealEstateService(FlatRepository()).detail_object(flat)
    #     context ={
    #         'flat': dto.__dict__,
    #     }
    #     print('ID',dto.id)
    #     return render(request, 'real_estate/delete_flat.html', context=context)
    # def post (self, request,pk):
    #     flat = Flat.objects.get(id=pk)
    #     print(flat.__dict__)
    #     flat.__dict__.pop('_state')
    #     flat.__dict__.pop('realestate_ptr_id')
    #     author = flat.__dict__.pop('author_id')
    #     distrcit = flat.__dict__.pop('district_id')
    #     city = flat.__dict__.pop('city_id')
    #     street = flat.__dict__.pop('street_id')
    #     data = FlatDTO(
    #         **flat.__dict__,
    #         author=author,
    #         city=city,
    #         district=distrcit,
    #         street=street,
    #     )
    #     RealEstateService(FlatRepository()).delete_object(data)
    #     return redirect('list_real_estates')

class HouseDeleteView(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = House
    template = 'real_estate/delete_house.html'
    redirect_success = 'list_user_real_estates'
    redirect_lose = 'create_house'
    model_dto = HouseDTO
    rep = HouseRepository
