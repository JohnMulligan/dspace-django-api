from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdvertisementList.as_view()),
    path('aggregations',views.AdvertisementAggregations.as_view()),
	path('autocomplete',views.AdvertisementTextFieldAutoComplete.as_view())
    ]
    
    