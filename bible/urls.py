from django.urls import path
from . import views

app_name = 'bible'

urlpatterns = [
    path('bible', view=views.BibleView.as_view(), name='bible'),
    path('mcheyne', view=views.McheyneView.as_view(), name='mcheyne'),
    path('bible/<str:book>/<int:chapter>', view=views.DataView.as_view(), name="bible_book")
]
