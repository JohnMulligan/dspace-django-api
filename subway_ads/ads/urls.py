from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdvertisementList.as_view()),
#     path('dataframes',views.VoyageDataFrames.as_view()),
#     path('caches',views.VoyageCaches.as_view()),
    path('aggregations',views.AdvertisementAggregations.as_view()),
	path('autocomplete',views.AdvertisementTextFieldAutoComplete.as_view()),
# 	path('groupby',views.VoyageGroupBy.as_view()),
# 	path('crosstabs',views.VoyageCrossTabs.as_view()),
# 	path('aggroutes',views.VoyageAggRoutes.as_view()),
# 	path('<int:voyage_id>/',views.SingleVoyage.as_view()),
# 	path('<int:voyage_id>/<varname>/',views.SingleVoyageVar.as_view())
    ]
    
    