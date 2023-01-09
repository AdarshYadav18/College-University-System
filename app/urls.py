from . import views
from django.urls import path

urlpatterns = [
    path('',views.savedemo),
    path('saveform',views.savedemo),
    path('display',views.displaydata),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.updatedata),
    path('delete/<int:id>',views.deletedata)
]
