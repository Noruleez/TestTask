from django.urls import path

from select_template.views import SelectTemplate

urlpatterns = [
    path('get_form/', SelectTemplate.as_view())
]
