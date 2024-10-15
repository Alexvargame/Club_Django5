import pprint

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from src.project.forms import ProjectCreateForm

from src.repositories import StackRepository, CategoryRepository

from src.project.project_service import ProjectService
from src.project.dtos.request.create_project_dto import CreateProjectDTO


class ProjectCreateView(LoginRequiredMixin, View):

    def get(self, request):
        return render(
            request,
            'project/create_project.html',
            context={
                "form": ProjectCreateForm(
                    stacks=StackRepository().list_stacks(),
                    categories=CategoryRepository().list_categories()

                )
            },
        )

    def post(self, request):
        form = ProjectCreateForm(request.POST,
                                 stacks=StackRepository().list_stacks(),
                                 categories=CategoryRepository().list_categories()
                                 )
        # for f in form.fields:
        #     print(f, type(f))
        print('CONTEXT', form.get_context())
        print('FORM', form)
        print(request.POST)
        if form.is_valid():
            # form.cleaned_data.pop("categories")
            # form.cleaned_data.pop("stacks")
            data = CreateProjectDTO(
                **form.cleaned_data,
                author_id=request.user.id,
                # categories=form['categories'].value(),#list(map(int, categories_str.split(","))),
                # stacks=form['stacks'].value(),#list(map(int, stacks_str.split(",")))
            )
            print(data)
            ProjectService().create_project(data)

            return redirect("list_project")
        return redirect("create_project")
