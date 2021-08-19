from django.shortcuts import render
from django.views.generic import View
from main.models import TeamMember, Corporation, Work
from .forms import EmailForm

class Home(View):
    def get(self, request):
        corporates = Corporation.objects.all()
        works = Work.objects.filter(displayOnLandingPage=True)
        context = {
            'corporates': corporates,
            'works': works
        }
        return render(request, 'main/home.html', context)


class About(View):
    def get(self, request):
        team_members = TeamMember.objects.all()
        works = Work.objects.filter(displayOnLandingPage=True)
        context = {
            'team_members': team_members,
            'works': works
        }
        return render(request, 'main/about.html', context)


class Portfolio(View):
    def get(self, request):
        works = Work.objects.all()
        context = {
            'works': works
        }
        return render(request, 'main/portfolio.html', context)


class Contact(View):
    def get(self, request):
        form = EmailForm()
        context = {
            'form': form
        }
        return render(request, 'main/contact.html', context)

    def post(self, request):
        form = EmailForm(data= request.POST)
        if form.is_valid():
            context = {
                'form': request.POST
            }
            return render(request, 'main/contact.html', context)
        else:
            context = {
                'form': form,
                'errors': form.errors
            }
            return render(request, 'main/contact.html', context)


class NotFound(View):
    def get(self, request):
        return render(request, 'main/notFound.html')
