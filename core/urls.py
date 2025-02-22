from django.urls import path
from .views import test_view, caregiver_view, patient_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", test_view.home, name="home"),
    path("patient/", test_view.home, name="patient-dashboard"),
    path("caretaker/", caregiver_view.home, name="caretaker-dashboard"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
