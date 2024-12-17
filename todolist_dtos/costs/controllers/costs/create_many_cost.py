from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import formset_factory
from decimal import Decimal

from django.contrib.auth.models import User


from todolist_dtos.models.category_cost import CategoryCost

from costs.repository import CostRepository
from costs.cost_service import CostService

from costs.dtos.request.cost_create_dto import CostCreateDTO
from costs.forms import CostManyCreateForm, CostForm

class CostManyCreateView(LoginRequiredMixin, View):

    def get(self, request):

        form = CostManyCreateForm
        SectionFormset = formset_factory(CostForm, extra=4)
        formset = SectionFormset()

        context = {
            'form': form,
            'formset': formset,
        }
        return render(request, 'costs/cost_many_create.html', context=context)

    def post(self, request):
        dto_lst = []
        sum_cost = 0
        b_form = CostManyCreateForm(request.POST)
        SectionFormset = formset_factory(CostForm, extra=4)
        b_formset = SectionFormset(request.POST)
        if b_form.is_valid() and b_formset.is_valid():
            user = User.objects.get(id=b_form['user'].value())
            category = CategoryCost.objects.get(id=b_form['category'].value())
            cost_date = b_form['cost_date'].value()
            for form in b_formset:
                if form['cost_name'].value() != '':
                    dto = CostCreateDTO(
                        user=user,
                        category=category,
                        cost_date=cost_date,
                        cost_name=form['cost_name'].value(),
                        cost_sum=Decimal(form['cost_sum'].value()),
                    )
                    dto_lst.append(dto)
                    sum_cost += dto.cost_sum
            CostService(CostRepository()).create_many_objects(dto_lst)
            user.profile.balance -= sum_cost
            user.profile.save()
            return redirect('costs_list_url')
        context = {
            'form': b_form,
            'formset': b_formset,
        }
        return render(request, 'costs/cost_many_create.html', context=context)

