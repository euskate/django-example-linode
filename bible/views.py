from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Abbreviation, BibleModel, McheyneModel

# Create your views here.
class BibleView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["abbr"] = Abbreviation.objects.all()
        context["bible"] = BibleModel.objects.all()
        return context
    
    template_name = 'bible/bible.html'

class McheyneView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mcheyne"] = McheyneModel.objects.all()
        return context
    
    template_name = 'bible/mcheyne.html'
