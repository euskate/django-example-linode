from django.shortcuts import render
from django.core import serializers
from django.views.generic import TemplateView
from .models import BibleMetaModel, BibleModel, McheyneModel
import datetime

# Create your views here.


class BibleView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta"] = BibleMetaModel.objects.all()
        context["meta_data"] = serializers.serialize('json', BibleMetaModel.objects.all())
        context["bible"] = BibleModel.objects.all()
        context["bible_data"] = serializers.serialize('json', BibleModel.objects.all())
        return context

    template_name = 'bible/bible.html'


class McheyneView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mcheyne"] = McheyneModel.objects.all()
        context["mcheyne_data"] = serializers.serialize('json', McheyneModel.objects.all())
        context["bible_data"] = serializers.serialize('json', BibleModel.objects.all())
        return context

    template_name = 'bible/mcheyne.html'
