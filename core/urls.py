from django.urls import path
from .views import test_view, caregiver_view, patient_view

urlpatterns = [
    path("", test_view.home, name="home"),
    path("patient/", test_view.home, name="patient-dashboard"),
    path("caretaker/", test_view.home, name="caretaker-dashboard"),
]