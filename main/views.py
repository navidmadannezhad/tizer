from django.shortcuts import render
from django.views.generic import View

class Home(View):
    def get(self, request):
        return render(request, 'main/home.html')


class About(View):
    def get(self, request):
        return render(request, 'main/about.html')


class Work(View):
    def get(self, request):
        return render(request, 'main/portfolio.html')


class Contact(View):
    def get(self, request):
        return render(request, 'main/contact.html')


class NotFound(View):
    def get(self, request):
        return render(request, 'main/notFound.html')
