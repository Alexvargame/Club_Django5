from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


from .forms import ProjectCreateForm

class ProjectCreateView(LoginRequiredMixin, View):

    def get(self, request):
        return render(
            request,
            'project/create_project.html',
            context={"form": ProjectCreateForm(initial={'author': request.user})},
        )

    def post(self, request):
        form = ProjectCreateForm(request.POST, initial={'author': request.user})
        print(request.POST)
        if form.is_valid():
            project = form.save()

            return redirect("list_project")
        return redirect("create_project")


class ProjectView(View):

    def get(self, request):
        context = {}#{'projects': Project.objects.all()}
        return render(request, 'project/list_projects.html', context=context)
