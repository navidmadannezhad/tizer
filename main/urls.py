from django.urls import path
from .views import Home, Work, About, Contact, NotFound

urlpatterns = [
    path('', Home.as_view()),
    path('contact/', Contact.as_view()),
    path('about/', About.as_view()),
    path('work/', Work.as_view()),

]
