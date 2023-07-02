import app.views

from django.urls import path

urlpatterns = [
    path('<str:module>/', app.views.SysView.as_view()),
    path('notices/<str:module>/', app.views.NoticesView.as_view()),
    path('offices/<str:module>/', app.views.OfficesView.as_view()),
    path('doctors/<str:module>/', app.views.DoctorsView.as_view()),
    path('patients/<str:module>/', app.views.PatientsView.as_view()),
    path('registes/<str:module>/', app.views.RegisteLogsView.as_view()),
]