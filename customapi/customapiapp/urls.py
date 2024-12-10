from django.urls import path
from customapiapp import views

urlpatterns=[
    path('',views.train_api_view),
    path('<int:id>',views.train_api_view),
    path('save',views.savefile)
]