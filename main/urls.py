from django.urls import path
from .views import Home, Work, About, Contact, NotFound

app_name = "main"

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('contact/', Contact.as_view(), name="contact"),
    path('about/', About.as_view(), name="about"),
    path('work/', Work.as_view(), name="work"),

]
