from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


app_name='diary'
urlpatterns=[
    path('',views.IndexView.as_view(),name="index"),
    path('hidden',views.TestView.as_view(),name="test"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
]