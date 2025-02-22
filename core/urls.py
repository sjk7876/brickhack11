from django.urls import path
from .views import test_view, caregiver_view, patient_view
from django.conf import settings
from django.conf.urls.static import static

app_name = "core"
urlpatterns = [
    path("", test_view.home, name="home"),
    path("patient/", patient_view.render_nodes, name="patient-dashboard"),
    path("caretaker/", caregiver_view.home, name="caretaker-dashboard"),
    path("patient/<int:node_id>/", patient_view.print_something, name="patient-node"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
