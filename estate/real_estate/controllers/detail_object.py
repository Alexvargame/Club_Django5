from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from real_estate.repository import FlatRepository, HouseRepository
from estate.repositories.comment_repository import CommentRepository

from estate.models.flat import Flat
from estate.models.house import House
from estate.models.real_estate import RealEstate
from real_estate.controllers.utils import ObjectDetailMixin, ObjectAllDetailMixin
from real_estate.forms import UserCommentForm, GuestCommetForm
from real_estate.dtos.request.create_comment_dto import CreateCommentDTO

class FlatDetailView(LoginRequiredMixin, ObjectDetailMixin, View):
    model = Flat
    template = 'real_estate/detail_flat.html'
    rep = FlatRepository

    # def get(self,request, pk):
    #     flat = Flat.objects.get(id=pk)
    #     dto = RealEstateService(FlatRepository()).detail_object(flat)
    #     context ={
    #         'flat': dto.__dict__
    #     }
    #
    #     return render(request, 'real_estate/detail_flat.html', context=context)


class HouseDetailView(LoginRequiredMixin, ObjectDetailMixin, View):
    model = House
    template = 'real_estate/detail_house.html'
    rep = HouseRepository

class HouseAllDetailView(ObjectAllDetailMixin, View):
    model = House
    model_comment = RealEstate
    template = 'real_estate/detail_house_for_all.html'
    rep = HouseRepository
    form_user = UserCommentForm
    form_guest = GuestCommetForm
    model_comment_dto = CreateCommentDTO
    rep_comment = CommentRepository

class FlatAllDetailView(ObjectAllDetailMixin, View):
    model = Flat
    model_comment = RealEstate
    template = 'real_estate/detail_flat_for_all.html'
    rep = FlatRepository
    form_user = UserCommentForm
    form_guest = GuestCommetForm
    model_comment_dto = CreateCommentDTO
    rep_comment = CommentRepository