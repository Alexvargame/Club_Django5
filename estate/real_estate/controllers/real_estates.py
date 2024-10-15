from django.views import View
from django.shortcuts import render

# from estate.models.flat import Flat
# from estate.models.house import House
from real_estate.real_estate_service import RealEstateService
from real_estate.repository import FlatRepository, HouseRepository

class RealEstateListView(View):

    def get(self, request):
        context = {
            'flats': RealEstateService(FlatRepository()).list_objects()[:3],#Flat.objects.all(),
            'houses': RealEstateService(HouseRepository()).list_objects()[:3]#House.objects.all()
        }
        return render(request, 'real_estate/list_real_estates.html', context=context)

class UserRealEstateListView(View):

    def get(self, request):
        context = {
            'flats': RealEstateService(FlatRepository()).user_list_objects(request.user),
            'houses': RealEstateService(HouseRepository()).user_list_objects(request.user)
        }
        return render(request, 'real_estate/list_user_real_estates.html', context=context)