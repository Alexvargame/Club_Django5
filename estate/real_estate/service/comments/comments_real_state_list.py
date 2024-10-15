from django.views import View
from django.shortcuts import render


from real_estate.real_estate_service import RealEstateService
from real_estate.repository import CommentRepository

class CommentsStateListView(View):

    def get(self, requet, rs=None):
        context = {
            'comments': RealEstateService(CommentRepository()).list_objects(rs)
        }
        return render(requet, 'real_estate/list_real_estates.html', context=context)