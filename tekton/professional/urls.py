from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^professional/$', views.ProfessionalList.as_view(), name='professional-list'),

]