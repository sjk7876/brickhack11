from django.urls import path
from .views import test_view, caregiver_view, patient_view

urlpatterns = [
    path("", test_view.home, name="home"),
    path("patient/", patient_view.render_nodes, name="patient-dashboard"),
    path("caretaker/", caregiver_view.home, name="caretaker-dashboard"),
]