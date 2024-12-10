from django.shortcuts import render


def main_menu(request):
    return render(request,'tasks/main_page.html')