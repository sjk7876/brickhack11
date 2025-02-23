from django.urls import path
from .views import test_view, caregiver_view, patient_view, auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", auth_view.index, name="index"),
    path("", auth_view.login, name="login"),
    path("logout", auth_view.logout, name="logout"),
    path("callback", auth_view.callback, name="callback"),
    path("patient/", patient_view.render_nodes, name="patient-dashboard"),
    path("caretaker/", caregiver_view.home, name="caretaker-dashboard"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
