from django.shortcuts import render
from django.core import serializers
from django.views.generic import TemplateView, View
from .models import BibleMetaModel, BibleModel, McheyneModel
from django.http import JsonResponse
import json
from datetime import datetime

# Create your views here.


class BibleView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta"] = BibleMetaModel.objects.all()
        # context["meta_data"] = serializers.serialize('json', BibleMetaModel.objects.all())
        # context["bible"] = BibleModel.objects.all()
        # context["bible_data"] = serializers.serialize('json', BibleModel.objects.all())
        return context

    template_name = 'bible/bible.html'


class McheyneView(TemplateView):
    def get_context_data(self, **kwargs):
        today = datetime.now()

        query = McheyneModel.objects.filter(
            month=today.month, day=today.day).get()
        item = vars(query)
        data = []
        for i in range(1, 5):
            id_rng = []
            for j in ['start', 'end']:
                book = item.get(f'part{i}_{j}_book')
                chapter = item.get(f'part{i}_{j}_chapter')
                verse = item.get(f'part{i}_{j}_verse')
                id_rng.append(BibleModel.objects.filter(
                    book=book, chapter=chapter, verse=verse).get().id)
            data.append(BibleModel.objects.filter(id__range=id_rng))

        list_data = [item.values() for item in data]
        context = super().get_context_data(**kwargs)
        context["today_mcheyne"] = query
        context["today_data"] = list_data
        # context["mcheyne_data"] = serializers.serialize('json', McheyneModel.objects.all())
        # context["bible_data"] = serializers.serialize('json', BibleModel.objects.all())
        return context

    template_name = 'bible/mcheyne.html'


class DataView(View):
    def get(self, request, book, chapter=0):
        if not chapter:
            data = BibleModel.objects.filter(book=book)
        else:
            data = BibleModel.objects.filter(book=book, chapter=chapter)
        list_data = list(data.values())

        # fields = [ field.name for field in BibleModel._meta.get_fields() ]
        # list_data = { i:r for i, r in enumerate(list(data.values())) }
        # print(dict(data.values())[:5])
        # json_data = json.dumps( list(data.values()) )
        return JsonResponse(list_data, safe=False, json_dumps_params={'ensure_ascii': False})
