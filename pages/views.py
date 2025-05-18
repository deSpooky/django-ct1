# from django.http import HttpResponse

# def home_page_view(request):
#     return HttpResponse("Hello, Spooky World!") 

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"