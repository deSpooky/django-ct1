from django.urls import path

# from .views import home_page_view

# urlpatterns = [
#     path ("", home_page_view, name="home")
# ]

from .views import HomePageView, AboutPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
