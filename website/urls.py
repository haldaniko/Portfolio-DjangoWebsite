from django.urls import path
from website.views import index

app_name = "website"

urlpatterns = [
    path('index/', index, name='index'),
    path('', index, name='index'),

]
