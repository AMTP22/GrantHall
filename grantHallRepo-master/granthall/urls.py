from django.urls import path

from . import views

app_name='granthall'

urlpatterns = [
	path('', views.index, name='home'),
	path('additem', views.additem, name='additem'),
	path('showitems', views.showitems, name='showitems'),
]
