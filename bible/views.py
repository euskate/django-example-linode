from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BibleMetaModel, BibleModel, McheyneModel

# Create your views here.


class BibleView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta"] = BibleMetaModel.objects.all()
        context["bible"] = BibleModel.objects.all()
        return context

    template_name = 'bible/bible.html'


class McheyneView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mcheyne"] = McheyneModel.objects.all()
        return context

    template_name = 'bible/mcheyne.html'
