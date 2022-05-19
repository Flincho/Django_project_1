from django.urls import path
from family_db.views import *


urlpatterns = [
    path('new_member/<str:name>/<str:last_name>/<birthday>/<kinship_deg>/<str:icecream_flavor>/', new_member),
    path('members/', members),
    path('get_member/<str:name>', get_member_by_name),
]
