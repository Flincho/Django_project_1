from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('probandotemplate/', probandoTemplate),
    path('diadehoy/', diaDeHoy),
    path('minombrees/<nombre>', miNombreEs),
    path('birthyear/<int:age>', birth_year),
    path('calculateage/<str:birth>', calculate_age),
    path('segundavista/', segunda_vista),
    path('identification_templates/<str:name>/<str:last_name>/', template_using_contxt),
    path('template_loader/<str:name>/<str:last_name>/', template_loader),
    path('new_group/<str:name>/<int:code>/', group_data),
    path('family_db/', include('family_db.urls')),

]
