from django.shortcuts import render, redirect
from django.views import View
from .services.client import ClientRequestService
from .dao import ServiceDAO
from .forms import ClientRequestForm

class HomeView(View):
    def get(self, request):
        services = ServiceDAO.get_all_services()
        return render(request, 'home.html', {'services': services})

class ConsultationView(View):
    def get(self, request, slug):
        service = ServiceDAO.get_service_by_slug(slug.lower())
        form = ClientRequestForm()
        return render(request, 'consultation/consultation.html', {'service': service, 'form': form})

    def post(self, request, slug):
        #service = ServiceDAO.get_service_by_slug(slug.lower())
        form = ClientRequestForm(request.POST)
        if form.is_valid():
            ClientRequestService().create_client_request(
                name=request.POST.get('name'),
                email = request.POST.get('email'),
                telegram = request.POST.get('telegram'),
                service_slug = slug,
                message = request.POST.get('message'),
            )


        # client_request_service = ClientRequestService()
        # client_request_service.create_client_request(name, email, telegram, service_id, message)
            return redirect('success_page')
        return render(request, 'consultation.html', {'form': form})

class SuccessView(View):
    def get(self, request):
        return render(request, 'consultation/success.html')