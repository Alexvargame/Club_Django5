from django.views import View
#from estate.models.flat import Flat

from django.contrib.auth.mixins import LoginRequiredMixin

from real_estate.forms import FlatSearchForm, HouseSearchForm
from real_estate.dtos.response.search_real_estate_dto import FlatSearchDTO, HouseSearchDTO
from real_estate.repository import FlatRepository, HouseRepository, SearchFlatRepository, SearchHouseRepository
from real_estate.service.search_objects.utils import ObjectSearchMixin


class FlatSearchView(LoginRequiredMixin, ObjectSearchMixin, View):
    form = FlatSearchForm
    template = 'real_estate/search_flat.html'
    model_dto = FlatSearchDTO
    model_rep = FlatRepository
    search_rep = SearchFlatRepository
    name_model = 'flats'
    initial = {'floor_at':1 ,'floor_to': 50, 'number_of_storeys_at': 1, 'number_of_storeys_to':50,
               'square_at': 1, 'square_to' :10000, 'price_at':1, 'price_to': 10000000, 'rooms_at':1,
               'rooms_to': 10,
               }

class HouseSearchView(LoginRequiredMixin, ObjectSearchMixin, View):
    form = HouseSearchForm
    template = 'real_estate/search_house.html'
    model_dto = HouseSearchDTO
    model_rep = HouseRepository
    search_rep = SearchHouseRepository
    name_model = 'houses'
    initial = {'area_at':1 ,'area_to': 50,  'square_at': 1, 'square_to' :10000, 'price_at':1,
               'price_to': 10000000, 'rooms_at':1,'rooms_to': 10,
                }