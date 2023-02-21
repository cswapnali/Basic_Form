from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('details/',views.form_details, name='form.html'),
]